import re
import openai

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

def get_video_transcript(video_id):
    pattern = r'\[.*?\]'
    response = YouTubeTranscriptApi.get_transcript(video_id)
    transcripts = [item['text'] for item in response]
    transcript_string = re.sub(pattern,'',' '.join(transcripts))
    return transcript_string

def summary_transcript(transcripts):
    prompt = 'please summarise the transcripts below into bullet points \n--\n"{0}"'.format(transcripts)
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        temperature = 0.1,
        max_tokens = 1000,
        messages = [
            {"role":"user","content":prompt}
        ]
     )
    return response.choices[0]['message']['content']