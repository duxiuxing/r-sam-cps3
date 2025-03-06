# R-Sam 认真玩 - CPS3 街机游戏


## 第三方文件说明

### image > playlist > playlist.png 和 playlist-content.png

RetraArch 使用的 CPS3 街机游戏列表图标文件。运行全能模拟器，通过“菜单 > 在线更新 > 更新素材”，可以把图标文件下载到本地的 assets > xmb > monochrome > png 文件夹。

- 项目网址：<https://github.com/libretro/retroarch-assets>
- 远程路径：xmb > monochrome > png

| 本地文件名 | 远程文件名 |
| :-- | :-- |
| playlist.png | Capcom - CP System III.png |
| playlist-content.png | Capcom - CP System III-content.png |


### pc-tool > Romcenter > firebird32

Romcenter 是一个 ROM 管理工具，可以导入 .dat 格式的数据库文件。如果 Romcenter 首次运行报错，可以把 firebird32 文件夹里的两个 .dll 文件拷贝到 Romcenter 的 firebird32 文件夹里再重试。

- 下载页面：<https://www.romcenter.com/downloadpage>
- .dll 文件来源：<https://firebirdsql.org/en/firebird-3-0>


### pc-tool > RDBEd-1.4.zip

.rdb 格式的数据库文件编辑器。

- 项目网址：<https://github.com/schellingb/RDBEd>


### pc-tool > WFC_conv_0-1.zip

生成 WiiFlow Cache 文件的命令行工具。

- 项目网址：<https://github.com/Wiimpathy/WFC_conv>


### third-party > Arcade - CPS3.csv

游戏名称的中英文对照。

- 项目网址：<https://github.com/duxiuxing/rom-name-cn>


### third-party > FinalBurn Neo (ClrMame Pro XML, Arcade only).dat

XML 格式的数据库文件，描述了 FinalBurn Neo 核心支持的街机 ROM 文件。可作为数据源导入到 Romcenter APP 中使用。

- 项目网址：<https://github.com/libretro/FBNeo>
- 远程路径：dats > FinalBurn Neo (ClrMame Pro XML, Arcade only).dat


### third-party > FBNeo - Arcade Games.rdb

RetroArch 使用的街机游戏数据库文件。运行全能模拟器，通过“菜单 > 在线更新 > 更新数据库”，可以把 .rdb 格式的数据库文件下载到本地的 database > rdb 文件夹。

- 项目网址：<https://github.com/libretro/libretro-database>
- 远程路径：rdb > FBNeo - Arcade Games.rdb


### wii > apps > retroarch-wii

只保留了 FB Alpha 2012 CPS-3 核心相关的文件。

- 项目网址：<https://github.com/libretro/fbalpha2012_cps3>
- 下载页面：<https://buildbot.libretro.com/stable>

retroarch.cfg 是 retroarch-wii 首次运行时自动生成的配置文件，由于 video_refresh_rate 是一个波动的值，为了同步方便，上库的时候手动设置成 60：
```ini
video_refresh_rate = "60"
```
