usage of git
添加文件：git add/rm 文件名
保存修改：git commit -m "注释内容"，如果注释内容过多，
			可以不要-m以及后面的说明，默认会启动文本编辑器来编辑注释文本
远程同步：git pull 下载github内容
		  git push pycode master提交文件到github的pycode目录，分支为master
查看远程信息：git remote -v
查看分支信息：git branch
切换分支： git checkout -b dev 创建并切换到新分支dev
		   git branch dev 创建分支dev
		   git checkout dev 切换到分支dev