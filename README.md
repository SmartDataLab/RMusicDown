## RMusicDown

playing and recommand music according with R

PPT可以嵌入音乐、vscode可以摸鱼听歌。Rmarkdown作为一种工作IDE和汇报展示的重要形式，不支持快捷的音乐查询、嵌入汇报文档以及敲代码跑实验的时候听歌。我们选择了两种路径实现了音乐的播放收听、同时后期支持推荐功能。
### Quick Start

```r
devtools::install_github('SmartDataLab/RMusicDown')
library(rmusicdown)
# now-playing-v2
now_playing_music("test")
# netease cloud music (playlist)
netease_music("代码",select=1)
```

### JS for Music

- Now Playing JS https://spinitron.github.io/v2-web-integration/widget.html

- control the element for JS https://www.w3schools.com/js/js_htmldom_elements.asp# RMusicDown
