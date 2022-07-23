# CATsama：定时发嘟的 Mastodon bot


在缪尚后厅和大家聊天时，猫猫从键盘经过，留下一串神秘文字。大家一致认为这是猫猫给我们留下的忠告，因此决定在缪尚给猫猫神开个位置，就有了这个喵喵喵账号。  
猫猫工作内容：每日上午八点半，在您的时间线上推送一个喵喵神签，或点名 ABC 的朋友们之一。  
详细搭建 bot 过程：[CATsama：如何做一个定时发嘟的 Mastodon bot](https://tech.musain.club/2022/07/12/catsama/)

## 安装
### python
在服务器上安装 miniconda：  

```
  wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
  sh Miniconda3-latest-Linux-x86_64.sh
```
### CATsama
安装喵喵 bot：  

```
  git clone https://github.com/melocery/CATsama.git
  cd CATsama
  conda create -n mastbot python=3.8
  conda activate mastbot
  pip3 install requests beautifulsoup4 Mastodon.py
  pip3 install numpy
```
## bot 账号
### 网页端操作
注册 Mastodon 账号，在管理面板找到开发-创建新应用，创建新应用并给予读写权限，复制访问令牌。  
由于 Fedi 有许多 bot 账号，为避免 bot 账号之间陷入无限回复循环，建议勾选账号设置中的 “这是一个机器人账户”。  
### 服务器端操作
创建 `mybot_usercred.secret` 并粘贴访问令牌：

```
  nano mybot_usercred.secret
```

上述完成后即可使用 `python catsama.py` 运行脚本。如果顺利，bot 就会发出嘟嘟；如有报错，根据报错信息修改。  

## 定时发嘟
使用 crontab 设置定时任务，定时自动运行 `python catsama.py` 即可实现定时发嘟。

```
  30 8 * * *  cd /root/miniconda/catsama && /root/miniconda3/envs/mastbot/bin/python catsama.py >> /root/miniconda/catsama/log.txt 2>&1
```
