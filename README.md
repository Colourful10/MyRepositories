# MyRepositories
#此篇谨用来记录10第一次成功实现vs code同步github代码，如果错误或者可以更方便的简化步骤 欢迎留言指正
0. 预先设定

git config --global user.name " "

git config --global user.email " "

1. 在github上，新建好自己的Responsitory
2. 在本地想要上传的文件夹下建立.sh文件，内容如下：

#!/bin/sh
git init 
git status  
git add .  
git commit -m 'add some code from Mac'
git remote add origin https://github.com/Colourful10/MyRepositories.git
git pull --rebase origin master   #domnload data
git push origin master            #upload data
git stash pop

上传，或者修改后上传，就是下图的样子
<img width="880" alt="image" src="https://user-images.githubusercontent.com/53842935/190886905-1778e7d6-74d2-41fe-9a19-bc6f68f87517.png">


关关难过关关过，把心态放轻，遇到问题慢慢查
