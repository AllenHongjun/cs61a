###
1. linux 虚拟机。 
2. ubuntu 18.04*64
3. 安装和使用 python3 64
4. vim emacs sublime vscode atom 这几个编辑器
5. powershell git-bash 熟悉使用命令行的工具
6. 只有一点代码的话 可以安装在c盘。。桌面上放一个实验和作业的文件。这样比较容易好找
7. 其他的资料可以放在其他盘。。然后整理
8. 这是学习一门编程语言。。同时 也是学习抽象的思维和方法。。如何解决复制的问题。。如何一步一步的抽象。
9. 同时做实验。。熟悉 数量 工具和编码使用。。
10. 也不是一定要安装和使用linux .如果要在虚拟机中使用 linux 会衍生出很多的问题。。慢慢再熟悉使用一下。。

不得不说powershell让压缩和解压缩变得更简单了。
Compress-Archive 和 Expand-Archive cmdlets 是 PowerShell v5 中的一大改进，大家看名字应该就不难猜出其功能，使用起来也非常简单。

#将文件或文件夹test压缩为test.zip
Compress-Archive -Path D:\test -DestinationPath E:\test.zip
1
2
#将文件test.zip解压到test目录下
Expand-Archive -Path E:\test.zip -DestinationPath F:\test
1
2
是吧，一句代码搞定~