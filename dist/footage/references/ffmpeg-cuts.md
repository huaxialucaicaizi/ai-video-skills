# ffmpeg 粗剪列表示例

```bash
# 虚构示例：按镜头表剪切后拼接（路径换成用户文件）
ffmpeg -y -ss 00:00:10 -to 00:00:18 -i input.mp4 -c copy shot01.mp4
ffmpeg -y -ss 00:00:40 -to 00:00:55 -i input.mp4 -c copy shot02.mp4
# concat demuxer 列表见 shot-list.txt（待 Mac 实测）
```

完整拼接与调色：**待 Mac 实测**。
