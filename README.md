Preview of the app
<img width="960" height="510" alt="Untitled1" src="https://github.com/user-attachments/assets/3dc3845d-fafc-4afe-b01c-eda26a8e8c6b" />

```markdown
# Audio Subtitle Generator

Generate precise subtitles from audio using OpenAI's Whisper model with word-level timing.

![App Preview](https://github.com/user-attachments/assets/3dc3845d-fafc-4afe-b01c-eda26a8e8c6b)

## Quick Start

1. **Install requirements:**
```bash
pip install whisperx tkinter
```

2. **Install FFmpeg:**
- Windows: `winget install FFmpeg`
- Mac: `brew install ffmpeg`
- Linux: `sudo apt install ffmpeg`

3. **Run the app:**
```bash
python whsperApp.py
```
output example 
[tax_tips.json](https://github.com/user-attachments/files/23291125/tax_tips.json)

## Features

- 🎯 Word-level & phrase-level timing
- 📁 Multiple formats: SRT, VTT, TXT, JSON
- ⚡ Simple one-file setup
- 🎵 Supports MP3, WAV, M4A files

![Sample Output](https://github.com/user-attachments/assets/110fa12a-7539-4d1b-8ab2-ce0bb128c6a0)

## Usage
[Uploading tax_tips.json…]()
{
  "language": "unknown",
  "segments": [
    {
      "start": 0.031,
      "end": 3.995,
      "text": " Once upon a rainy evening, I found an old notebook in my attic.",
      "words": [
        {
          "word": "Once",
          "start": 0.031,
          "end": 0.351,
          "score": 0.753
        },
        {
          "word": "upon",
          "start": 0.471,
          "end": 0.692,
          "score": 0.915
        },
        {
          "word": "a",
          "start": 0.752,
          "end": 0.772,
          "score": 0.999
        },
        {
          "word": "rainy",
          "start": 0.832,
          "end": 1.112,
          "score": 0.885
        },
        {
          "word": "evening,",
          "start": 1.232,
          "end": 1.532,
          "score": 0.766
        },
        {
          "word": "I",
          "start": 2.073,
          "end": 2.153,
          "score": 0.713
        },
        {
          "word": "found",
          "start": 2.253,
          "end": 2.513,
          "score": 0.834
        },
        {
          "word": "an",
          "start": 2.573,
          "end": 2.613,
          "score": 0.997
        },
        {
          "word": "old",
          "start": 2.773,
          "end": 2.934,
          "score": 0.541
        },
        {
          "word": "notebook",
          "start": 2.994,
          "end": 3.354,
          "score": 0.872
        },
        {
          "word": "in",
          "start": 3.414,
          "end": 3.474,
          "score": 0.966
        },
        {
          "word": "my",
          "start": 3.514,
          "end": 3.614,
          "score": 0.982
        },
        {
          "word": "attic.",
          "start": 3.734,
          "end": 3.995,
          "score": 0.998
        }
      ]
    },
    {
      "start": 5.676,
      "end": 8.258,
      "text": "It wasn't mine yet every page had my handwriting.",
      "words": [
        {
          "word": "It",
          "start": 5.676,
          "end": 5.716,
          "score": 0.964
        },
        {
          "word": "wasn't",
          "start": 5.776,
          "end": 6.036,
          "score": 0.75
        },
        {
          "word": "mine",
          "start": 6.076,
          "end": 6.337,
          "score": 0.792
        },
        {
          "word": "yet",
          "start": 6.377,
          "end": 6.577,
          "score": 0.733
        },
        {
          "word": "every",
          "start": 6.777,
          "end": 7.017,
          "score": 0.829
        },
        {
          "word": "page",
          "start": 7.077,
          "end": 7.378,
          "score": 0.945
        },
        {
          "word": "had",
          "start": 7.438,
          "end": 7.558,
          "score": 0.808
        },
        {
          "word": "my",
          "start": 7.598,
          "end": 7.698,
          "score": 0.952
        },
        {
          "word": "handwriting.",
          "start": 7.758,
          "end": 8.258,
          "score": 0.847
        }
      ]
    },
    {
      "start": 9.239,
      "end": 10.14,
      "text": "A confused tone.",
      "words": [
        {
          "word": "A",
          "start": 9.239,
          "end": 9.279,
          "score": 0.787
        },
        {
          "word": "confused",
          "start": 9.319,
          "end": 9.82,
          "score": 0.801
        },
        {
          "word": "tone.",
          "start": 9.86,
          "end": 10.14,
          "score": 0.924
        }
      ]
    },
    {
      "start": 10.841,
      "end": 14.424,
      "text": "The first line said, don't be afraid you've lived this day before.",
      "words": [
        {
          "word": "The",
          "start": 10.841,
          "end": 10.941,
          "score": 0.786
        },
        {
          "word": "first",
          "start": 10.981,
          "end": 11.201,
          "score": 0.699
        },
        {
          "word": "line",
          "start": 11.261,
          "end": 11.501,
          "score": 0.542
        },
        {
          "word": "said,",
          "start": 11.541,
          "end": 11.762,
          "score": 0.929
        },
        {
          "word": "don't",
          "start": 11.802,
          "end": 12.562,
          "score": 0.71
        },
        {
          "word": "be",
          "start": 12.622,
          "end": 12.682,
          "score": 0.762
        },
        {
          "word": "afraid",
          "start": 12.742,
          "end": 13.043,
          "score": 0.809
        },
        {
          "word": "you've",
          "start": 13.083,
          "end": 13.363,
          "score": 0.915
        },
        {
          "word": "lived",
          "start": 13.423,
          "end": 13.623,
          "score": 0.766
        },
        {
          "word": "this",
          "start": 13.663,
          "end": 13.823,
          "score": 0.669
        },
        {
          "word": "day",
          "start": 13.883,
          "end": 14.024,
          "score": 0.937
        },
        {
          "word": "before.",
          "start": 14.064,
          "end": 14.424,
          "score": 0.88
        }
      ]
    },
    {
      "start": 15.425,
      "end": 15.845,
      "text": "Pause.",
      "words": [
        {
          "word": "Pause.",
          "start": 15.425,
          "end": 15.845,
          "score": 0.98
        }
      ]
    },
    {
      "start": 16.746,
      "end": 19.288,
      "text": "I smiled, closed the book and whispered.",
      "words": [
        {
          "word": "I",
          "start": 16.746,
          "end": 16.806,
          "score": 0.98
        },
        {
          "word": "smiled,",
          "start": 16.906,
          "end": 17.327,
          "score": 0.812
        },
        {
          "word": "closed",
          "start": 17.867,
          "end": 18.147,
          "score": 0.82
        },
        {
          "word": "the",
          "start": 18.187,
          "end": 18.247,
          "score": 1.0
        },
        {
          "word": "book",
          "start": 18.287,
          "end": 18.468,
          "score": 0.819
        },
        {
          "word": "and",
          "start": 18.728,
          "end": 18.808,
          "score": 0.91
        },
        {
          "word": "whispered.",
          "start": 18.888,
          "end": 19.288,
          "score": 0.844
        }
      ]
    },
    {
      "start": 20.189,
      "end": 22.892,
      "text": "Then maybe this time, I'll make it right.",
      "words": [
        {
          "word": "Then",
          "start": 20.189,
          "end": 20.329,
          "score": 0.955
        },
        {
          "word": "maybe",
          "start": 20.429,
          "end": 20.69,
          "score": 0.99
        },
        {
          "word": "this",
          "start": 20.73,
          "end": 20.87,
          "score": 0.782
        },
        {
          "word": "time,",
          "start": 20.93,
          "end": 21.17,
          "score": 0.988
        },
        {
          "word": "I'll",
          "start": 22.271,
          "end": 22.411,
          "score": 0.8
        },
        {
          "word": "make",
          "start": 22.431,
          "end": 22.551,
          "score": 0.738
        },
        {
          "word": "it",
          "start": 22.591,
          "end": 22.631,
          "score": 0.505
        },
        {
          "word": "right.",
          "start": 22.691,
          "end": 22.892,
          "score": 0.756
        }
      ]
    },
    {
      "start": 23.772,
      "end": 24.493,
      "text": "Ten to laugh.",
      "words": [
        {
          "word": "Ten",
          "start": 23.772,
          "end": 23.973,
          "score": 0.933
        },
        {
          "word": "to",
          "start": 24.013,
          "end": 24.133,
          "score": 0.932
        },
        {
          "word": "laugh.",
          "start": 24.193,
          "end": 24.493,
          "score": 0.831
        }
      ]
    },
    {
      "start": 25.334,
      "end": 28.076,
      "text": "Funny how fate sometimes leaves reminders and dust.",
      "words": [
        {
          "word": "Funny",
          "start": 25.334,
          "end": 25.634,
          "score": 0.952
        },
        {
          "word": "how",
          "start": 25.734,
          "end": 25.874,
          "score": 0.94
        },
        {
          "word": "fate",
          "start": 25.954,
          "end": 26.215,
          "score": 0.977
        },
        {
          "word": "sometimes",
          "start": 26.275,
          "end": 26.775,
          "score": 0.811
        },
        {
          "word": "leaves",
          "start": 26.835,
          "end": 27.075,
          "score": 0.791
        },
        {
          "word": "reminders",
          "start": 27.135,
          "end": 27.596,
          "score": 0.869
        },
        {
          "word": "and",
          "start": 27.676,
          "end": 27.736,
          "score": 0.806
        },
        {
          "word": "dust.",
          "start": 27.776,
          "end": 28.076,
          "score": 0.885
        }
      ]
    },
    {
      "start": 28.897,
      "end": 30.038,
      "text": "The rain stopped.",
      "words": [
        {
          "word": "The",
          "start": 28.897,
          "end": 28.997,
          "score": 0.937
        },
        {
          "word": "rain",
          "start": 29.037,
          "end": 29.277,
          "score": 0.895
        },
        {
          "word": "stopped.",
          "start": 29.337,
          "end": 30.038,
          "score": 0.86
        }
      ]
    },
    {
      "start": 30.018,
      "end": 31.49,
      "text": " and so did time.",
      "words": [
        {
          "word": "and",
          "start": 30.018,
          "end": 30.764,
          "score": 0.65
        },
        {
          "word": "so",
          "start": 30.826,
          "end": 30.972,
          "score": 0.889
        },
        {
          "word": "did",
          "start": 31.034,
          "end": 31.137,
          "score": 0.905
        },
        {
          "word": "time.",
          "start": 31.179,
          "end": 31.49,
          "score": 0.836
        }
      ]
    }
  ]
}
1. Click "Browse" to select audio file
2. Choose output format and timing level
3. Click "Generate Subtitles"
4. Find output file in same folder as input
5. 3 options are given to export subtitles (json , vtt , srt)

**Star if you find this useful! ⭐**
```

Word level subtitle feature will be available soon in srt and vtt format

Todo (Dated : 19 nov 2025)  : Make it load once not everytime
                              add other video processing tools as a combined tool

