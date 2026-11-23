# ffmpeg 切片示例

```bash
ffmpeg -y -ss 00:12:30 -to 00:13:05 -i long.mp4 -c copy clip_01.mp4
# 竖屏再构图示例（待 Mac 实测调参）
# ffmpeg -i clip_01.mp4 -vf "crop=ih*9/16:ih,scale=1080:1920" clip_01_v.mp4
```
