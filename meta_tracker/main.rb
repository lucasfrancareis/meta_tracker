require 'json'

puts "_"*50
puts "Bem vindo ao Meta Tracker!"
puts "\n"*2
puts "Digite sua url para a transcrição: "
puts "\n"*2

url = gets.chomp

saida = `python transcript.py "#{url}"`.strip

resultado = JSON.parse(saida)


transcript = resultado["transcript"]
puts "_"*50
puts "\n"*2
puts "✅Transcrição finalizada✅"
puts transcript


# url = gets.chomp
# url = url.split('&')[0]

# audio_path = "audio.mp3"
# system("yt-dlp -x --audio-format mp3 -o \"#{audio_path}\" \"#{url}\"")

# if File.exist?(audio_path)
#   transcribe_audio(audio_path)
# else
#   puts "❌Não foi possivel transcrever este video❌"
# end
