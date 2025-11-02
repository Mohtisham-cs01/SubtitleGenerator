import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox
import whisperx
import torch
import json
import threading
from pathlib import Path


class SubtitleGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WhisperX Subtitle Generator")
        self.root.geometry("1000x700")
        
        # Variables
        self.audio_path = tk.StringVar()
        self.transcript_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.model_size = tk.StringVar(value="base")
        self.language = tk.StringVar(value="en")
        self.device = tk.StringVar(value="cuda" if torch.cuda.is_available() else "cpu")
        self.mode = tk.StringVar(value="transcribe")
        
        self.processing = False
        self.result_data = None
        
        self.create_widgets()
    
    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # ===== MODE SELECTION =====
        mode_frame = ttk.LabelFrame(main_frame, text="Mode", padding="10")
        mode_frame.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Radiobutton(mode_frame, text="Audio → Transcript & Subtitles (Full Transcription)", 
                       variable=self.mode, value="transcribe", 
                       command=self.update_mode).grid(row=0, column=0, sticky=tk.W, padx=5)
        ttk.Radiobutton(mode_frame, text="Audio + Transcript → Subtitles (Alignment Only - Faster)", 
                       variable=self.mode, value="align", 
                       command=self.update_mode).grid(row=0, column=1, sticky=tk.W, padx=5)
        
        # ===== INPUT SECTION =====
        input_frame = ttk.LabelFrame(main_frame, text="Inputs", padding="10")
        input_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        input_frame.columnconfigure(1, weight=1)
        
        # Audio file
        ttk.Label(input_frame, text="Audio File:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(input_frame, textvariable=self.audio_path).grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        ttk.Button(input_frame, text="Browse", command=self.browse_audio).grid(row=0, column=2, padx=5)
        
        # Transcript file (for alignment mode)
        self.transcript_label = ttk.Label(input_frame, text="Transcript File:")
        self.transcript_entry = ttk.Entry(input_frame, textvariable=self.transcript_path)
        self.transcript_button = ttk.Button(input_frame, text="Browse", command=self.browse_transcript)
        
        # Transcript text area (for alignment mode)
        ttk.Label(input_frame, text="Or Paste Transcript:").grid(row=2, column=0, sticky=(tk.W, tk.N), pady=5)
        self.transcript_text = scrolledtext.ScrolledText(input_frame, height=4, wrap=tk.WORD)
        self.transcript_text.grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        # ===== SETTINGS SECTION =====
        settings_frame = ttk.LabelFrame(main_frame, text="Settings", padding="10")
        settings_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Model size
        ttk.Label(settings_frame, text="Model Size:").grid(row=0, column=0, sticky=tk.W, pady=5, padx=5)
        self.model_combo = ttk.Combobox(settings_frame, textvariable=self.model_size, 
                                       values=["tiny", "base", "small", "medium", "large-v3"],
                                       state="readonly", width=15)
        self.model_combo.grid(row=0, column=1, sticky=tk.W, pady=5)
        ttk.Label(settings_frame, text="(base recommended)", foreground="gray").grid(row=0, column=2, sticky=tk.W, padx=5)
        
        # Language
        ttk.Label(settings_frame, text="Language:").grid(row=1, column=0, sticky=tk.W, pady=5, padx=5)
        lang_combo = ttk.Combobox(settings_frame, textvariable=self.language, 
                                 values=["auto", "en", "es", "fr", "de", "it", "pt", "nl", "pl", "ru", "zh", "ja", "ko"],
                                 state="readonly", width=15)
        lang_combo.grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # Device
        ttk.Label(settings_frame, text="Device:").grid(row=2, column=0, sticky=tk.W, pady=5, padx=5)
        device_combo = ttk.Combobox(settings_frame, textvariable=self.device, 
                                   values=["cuda", "cpu"], state="readonly", width=15)
        device_combo.grid(row=2, column=1, sticky=tk.W, pady=5)
        
        # Output path
        ttk.Label(settings_frame, text="Output Folder:").grid(row=3, column=0, sticky=tk.W, pady=5, padx=5)
        ttk.Entry(settings_frame, textvariable=self.output_path, width=40).grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)
        ttk.Button(settings_frame, text="Browse", command=self.browse_output).grid(row=3, column=2, padx=5)
        
        # ===== PROCESS BUTTON =====
        self.process_button = ttk.Button(main_frame, text="Generate Subtitles", 
                                        command=self.process, style="Accent.TButton")
        self.process_button.grid(row=3, column=0, columnspan=3, pady=10)
        
        # ===== PROGRESS =====
        self.progress_label = ttk.Label(main_frame, text="Ready", foreground="green")
        self.progress_label.grid(row=4, column=0, columnspan=3)
        
        self.progress_bar = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress_bar.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        # ===== PREVIEW SECTION =====
        preview_frame = ttk.LabelFrame(main_frame, text="Preview", padding="10")
        preview_frame.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        preview_frame.columnconfigure(0, weight=1)
        preview_frame.rowconfigure(0, weight=1)
        
        # Preview text with scrollbar
        self.preview_text = scrolledtext.ScrolledText(preview_frame, height=15, wrap=tk.WORD)
        self.preview_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Export buttons
        export_frame = ttk.Frame(preview_frame)
        export_frame.grid(row=1, column=0, pady=(10, 0))
        
        ttk.Button(export_frame, text="Export as SRT", command=lambda: self.export_subtitles("srt")).pack(side=tk.LEFT, padx=5)
        ttk.Button(export_frame, text="Export as VTT", command=lambda: self.export_subtitles("vtt")).pack(side=tk.LEFT, padx=5)
        ttk.Button(export_frame, text="Export as JSON", command=lambda: self.export_subtitles("json")).pack(side=tk.LEFT, padx=5)
        
        # Configure grid weights for main_frame
        main_frame.rowconfigure(6, weight=1)
        
        # Initial mode update
        self.update_mode()
    
    def update_mode(self):
        """Update UI based on selected mode"""
        if self.mode.get() == "align":
            # Show transcript input
            self.transcript_label.grid(row=1, column=0, sticky=tk.W, pady=5)
            self.transcript_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5)
            self.transcript_button.grid(row=1, column=2, padx=5)
            self.transcript_text.grid()
            # Disable model selection for alignment
            self.model_combo.config(state="disabled")
        else:
            # Hide transcript input
            self.transcript_label.grid_remove()
            self.transcript_entry.grid_remove()
            self.transcript_button.grid_remove()
            self.transcript_text.grid_remove()
            # Enable model selection
            self.model_combo.config(state="readonly")
    
    def browse_audio(self):
        filename = filedialog.askopenfilename(
            title="Select Audio File",
            filetypes=[("Audio Files", "*.mp3 *.wav *.m4a *.flac *.ogg"), ("All Files", "*.*")]
        )
        if filename:
            self.audio_path.set(filename)
            # Auto-set output path
            if not self.output_path.get():
                self.output_path.set(str(Path(filename).parent))
    
    def browse_transcript(self):
        filename = filedialog.askopenfilename(
            title="Select Transcript File",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filename:
            self.transcript_path.set(filename)
            # Load transcript content
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    self.transcript_text.delete(1.0, tk.END)
                    self.transcript_text.insert(1.0, f.read())
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read transcript: {str(e)}")
    
    def browse_output(self):
        folder = filedialog.askdirectory(title="Select Output Folder")
        if folder:
            self.output_path.set(folder)
    
    def update_progress(self, message, color="blue"):
        self.progress_label.config(text=message, foreground=color)
        self.root.update_idletasks()
    
    def process(self):
        """Main processing function"""
        if self.processing:
            return
        
        # Validate inputs
        if not self.audio_path.get():
            messagebox.showerror("Error", "Please select an audio file")
            return
        
        if self.mode.get() == "align":
            transcript_content = self.transcript_text.get(1.0, tk.END).strip()
            if not transcript_content and not self.transcript_path.get():
                messagebox.showerror("Error", "Please provide a transcript (file or text)")
                return
        
        if not self.output_path.get():
            self.output_path.set(str(Path(self.audio_path.get()).parent))
        
        # Start processing in a thread
        self.processing = True
        self.process_button.config(state="disabled")
        self.progress_bar.start()
        
        thread = threading.Thread(target=self.process_worker)
        thread.daemon = True
        thread.start()
    
    def process_worker(self):
        """Worker thread for processing"""
        try:
            if self.mode.get() == "transcribe":
                self.transcribe_audio()
            else:
                self.align_transcript()
            
            self.root.after(0, lambda: self.update_progress("Processing complete!", "green"))
            self.root.after(0, self.display_preview)
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"Processing failed: {str(e)}"))
            self.root.after(0, lambda: self.update_progress("Error occurred", "red"))
        finally:
            self.processing = False
            self.root.after(0, lambda: self.process_button.config(state="normal"))
            self.root.after(0, self.progress_bar.stop)
    
    def transcribe_audio(self):
        """Full transcription"""
        self.root.after(0, lambda: self.update_progress("Loading Whisper model..."))
        
        device = self.device.get()
        compute_type = "float16" if device == "cuda" else "int8"
        language = None if self.language.get() == "auto" else self.language.get()
        
        model = whisperx.load_model(
            self.model_size.get(),
            device,
            compute_type=compute_type,
            language=language
        )
        
        self.root.after(0, lambda: self.update_progress("Loading audio..."))
        audio = whisperx.load_audio(self.audio_path.get())
        
        self.root.after(0, lambda: self.update_progress("Transcribing audio..."))
        result = model.transcribe(audio, batch_size=16)
        
        self.root.after(0, lambda: self.update_progress("Loading alignment model..."))
        model_a, metadata = whisperx.load_align_model(
            language_code=result["language"],
            device=device
        )
        
        self.root.after(0, lambda: self.update_progress("Aligning transcript..."))
        result = whisperx.align(
            result["segments"],
            model_a,
            metadata,
            audio,
            device,
            return_char_alignments=False
        )
        
        self.result_data = {
            "language": result.get("language", "unknown"),
            "segments": result["segments"]
        }
    
    def align_transcript(self):
        """Align existing transcript"""
        self.root.after(0, lambda: self.update_progress("Loading audio..."))
        
        device = self.device.get()
        audio = whisperx.load_audio(self.audio_path.get())
        
        # Get transcript text
        transcript_content = self.transcript_text.get(1.0, tk.END).strip()
        
        self.root.after(0, lambda: self.update_progress("Loading alignment model..."))
        model_a, metadata = whisperx.load_align_model(
            language_code=self.language.get(),
            device=device
        )
        
        # Create segments
        segments = [{
            "start": 0,
            "end": len(audio) / 16000,
            "text": transcript_content
        }]
        
        self.root.after(0, lambda: self.update_progress("Aligning transcript with audio..."))
        result = whisperx.align(
            segments,
            model_a,
            metadata,
            audio,
            device,
            return_char_alignments=False
        )
        
        self.result_data = {
            "language": self.language.get(),
            "segments": result["segments"]
        }
    
    def display_preview(self):
        """Display preview of subtitles"""
        if not self.result_data:
            return
        
        self.preview_text.delete(1.0, tk.END)
        
        preview = f"Language: {self.result_data['language']}\n"
        preview += f"Total segments: {len(self.result_data['segments'])}\n"
        
        # Count total words
        total_words = sum(len(seg.get('words', [])) for seg in self.result_data['segments'])
        preview += f"Total words: {total_words}\n"
        preview += "=" * 60 + "\n\n"
        
        # Preview segments
        preview += "SEGMENT-LEVEL PREVIEW:\n"
        preview += "-" * 60 + "\n"
        for i, segment in enumerate(self.result_data['segments'][:5], 1):
            start = self.format_timestamp(segment['start'])
            end = self.format_timestamp(segment['end'])
            preview += f"{i}\n{start} --> {end}\n{segment['text'].strip()}\n\n"
        
        # Preview word-level
        preview += "\nWORD-LEVEL PREVIEW:\n"
        preview += "-" * 60 + "\n"
        word_count = 0
        for segment in self.result_data['segments'][:10]:
            if 'words' in segment:
                for word in segment['words']:
                    start = self.format_timestamp(word['start'])
                    end = self.format_timestamp(word['end'])
                    preview += f"{start} --> {end}: {word['word']}\n"
                    word_count += 1
                    if word_count >= 30:  # Show first 30 words
                        break
            if word_count >= 30:
                break
        
        if total_words > 30:
            preview += f"\n... and {total_words - 30} more words"
        
        self.preview_text.insert(1.0, preview)
    
    def format_timestamp(self, seconds, format_type="srt"):
        """Format timestamp for subtitles"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds % 1) * 1000)
        
        if format_type == "srt":
            return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"
        else:  # vtt
            return f"{hours:02d}:{minutes:02d}:{secs:02d}.{millis:03d}"
    
    def export_subtitles(self, format_type):
        """Export subtitles in specified format"""
        if not self.result_data:
            messagebox.showwarning("Warning", "No data to export. Please process audio first.")
            return
        
        audio_name = Path(self.audio_path.get()).stem
        default_name = f"{audio_name}.{format_type}"
        
        filename = filedialog.asksaveasfilename(
            title=f"Save {format_type.upper()} File",
            initialdir=self.output_path.get(),
            initialfile=default_name,
            defaultextension=f".{format_type}",
            filetypes=[(f"{format_type.upper()} Files", f"*.{format_type}"), ("All Files", "*.*")]
        )
        
        if not filename:
            return
        
        try:
            if format_type == "json":
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(self.result_data, f, indent=2, ensure_ascii=False)
            elif format_type == "srt":
                self.export_srt(filename)
            elif format_type == "vtt":
                self.export_vtt(filename)
            
            messagebox.showinfo("Success", f"Exported to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Export failed: {str(e)}")
    
    def export_srt(self, filename):
        """Export as SRT format"""
        with open(filename, 'w', encoding='utf-8') as f:
            for i, segment in enumerate(self.result_data['segments'], 1):
                start = self.format_timestamp(segment['start'], "srt")
                end = self.format_timestamp(segment['end'], "srt")
                f.write(f"{i}\n")
                f.write(f"{start} --> {end}\n")
                f.write(f"{segment['text'].strip()}\n\n")
    
    def export_vtt(self, filename):
        """Export as VTT format"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("WEBVTT\n\n")
            for segment in self.result_data['segments']:
                start = self.format_timestamp(segment['start'], "vtt")
                end = self.format_timestamp(segment['end'], "vtt")
                f.write(f"{start} --> {end}\n")
                f.write(f"{segment['text'].strip()}\n\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = SubtitleGeneratorApp(root)
    root.mainloop()