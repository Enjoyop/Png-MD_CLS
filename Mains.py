import binascii
import os

folder_path = "D:/Users/PngClear"

for filename in os.listdir(folder_path):
	if filename.endswith('.png'):
		file_path = os.path.join(folder_path, filename);
		with open(file_path, 'rb') as file:
			data = file.read();
			print(file);

		start_pattern = b'\x00\x19\x74\x45\x58';
		end_pattern = b'\x49\x44\x41\x54';

		start = data.find(start_pattern);
		if start != -1:
			end = data.find(end_pattern, start+len(start_pattern));
			if end != -1:

				data = data[:start] + data[end-len(end_pattern) + 2:];

				with open(file_path, 'wb') as file:
					file.write(data);
