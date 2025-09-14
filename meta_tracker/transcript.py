# from youtube_transcript_api import YouTubeTranscriptApi
# import json
# import re
# import sys
# import os


# def extract_video_id(url):
#     match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
#     if match:
#         return match.group(1)
#     else:
#         raise ValueError("❌ Link inválido")


# def get_transcription(video_id):
#     print("Transcrevendo video⏳", file=sys.stderr)
#     transcript = YouTubeTranscriptApi.get_transcript(video_id)  # type: ignore
#     return transcript


# def save_to_json(url, transcript):
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(base_dir, "meta_data.json")

#     if os.path.exists(file_path):
#         with open(file_path, "r", encoding="utf-8") as f:
#             try:
#                 data = json.load(f)
#             except json.JSONDecodeError:
#                 data = []
#     else:
#         data = []

#     if not isinstance(data, list):
#         data = [data]

#     data.append({
#         "url": url,
#         "transcript": transcript
#     })

#     with open(file_path, "w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=2)

#     print("✅Transcrição salva em: meta_data.json", file=sys.stderr)

# # def save_to_json(url, transcript):

# #     base_dir = os.path.dirname(os.path.abspath(__file__))
# #     file_path = os.path.join(base_dir, "meta_data.json")

# #     data = {
# #         "url": url,
# #         "transcript": transcript
# #     }

# #     with open(file_path, "w", encoding="utf-8") as all:
# #         json.dump(data, all, ensure_ascii=False, indent=2)
# #     print("✅Transcrição salva em: meta_data.json", file=sys.stderr)


# def process_video(url):
#     video_id = extract_video_id(url)
#     transcript = get_transcription(video_id)
#     save_to_json(url, transcript)
#     return transcript


# if __name__ == "__main__":
#     url = sys.argv[1]
#     try:  # type: ignore
#         transcript = process_video(url)
#         print(json.dumps({"transcript": transcript}, ensure_ascii=False))
#     except Exception as e:
#         print(json.dumps({"Error": str(e)}, ensure_ascii=False))
#         sys.exit(1)


from youtube_transcript_api import YouTubeTranscriptApi
import json
import re
import sys
import os


def extract_video_id(url):
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
    if match:
        return match.group(1)
    else:
        raise ValueError("❌ Link inválido")


def get_transcription(video_id):
    print("Transcrevendo vídeo⏳", file=sys.stderr)
    # Pega o transcript
    transcript_obj = YouTubeTranscriptApi.list_transcripts(
        video_id).find_transcript(['pt', 'en'])
    transcript = transcript_obj.fetch()
    return transcript


def save_to_json(url, transcript):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "meta_data.json")

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    if not isinstance(data, list):
        data = [data]

    data.append({
        "url": url,
        "transcript": transcript
    })

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("✅ Transcrição salva em: meta_data.json", file=sys.stderr)


def process_video(url):
    try:
        video_id = extract_video_id(url)
        transcript = get_transcription(video_id)
        save_to_json(url, transcript)
        return transcript
    except Exception as e:
        print(f"❌ Erro ao processar o vídeo: {e}", file=sys.stderr)
        raise


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"Error": "Nenhuma URL fornecida"}))
        sys.exit(1)

    url = sys.argv[1]
    try:
        transcript = process_video(url)
        print(json.dumps({"transcript": transcript}, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"Error": str(e)}, ensure_ascii=False))
        sys.exit(1)
