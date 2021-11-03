# Linux指令
    ● grep -nr  "xxxxx"  /etc/    或	grep -E 'k1|k2'
    ● find /etc/ -name rc.local
    ● du -hd 1   查看一级目录大小
    ● chown -R wangshize:wangshize /filename     递归修改文件所属
    ● ln -sf  目标名  软连接名
    ● cat /proc/cmdline   可以看bootargs
    ● ps -T pid 查看线程
    ● lsof  看进程打开的文件描述符
    ● cat /dev/null > xxx  清空文件
    ● ! number 执行第几条历史命令， echo $?  看上一条命令返回值
    ● su 切换用户（没写用户默认root）， sudo 提升权限
    ● telnet  *.*.*.* portnum   只能用于测试TCP端口
    ● 命令1 && 命令2 || 命令3   :前一条执行成功才执行第二条，否则执行命令3
        命令1;  命令2   :不管前一条执行是否成功，都会执行第二条

    ● 烧写uboot
    echo 0 > 
    /sys/block/mmcblk1boot0/force_ro
    dd if=uboot. imx  of=/dev/mmcblk1boot0  bs=1  seek=1024

    ● 终端直接向串口发送数据
        ○ stty
        ○ hexdump -C /dev/ttymxc4
        ○ echo -e -n "\x7e\x01\xf5\x11" > /dev/ttymxc4

    ● 时间
        ○ date -s "2020-11-1 18:45:34"	设置系统时间
        ○ hwclock -w		写入硬件时间
        ○ hwclock -r  		读取硬件时间
        ○ 系统时间或RTC时钟在启动后被修改（系统启动日志有修改打印）：是被systemd修改（不能超过systemd构建时间，可看其源码）

    ● 创建ext4
        ○ dd if=/dev/zero of=rootfs.ext4 bs=1M count=1536
        ○ mkfs.ext4 rootfs.ext4
        ○ mkdir rootfs
        ○ mount rootfs.ext4 rootfs

    ● 挂载
        ○ mount -t nfs -o nolock 192.168.1.22:/home/wsz /mnt
        ○ mount -t vfat /dev/sda1 /mnt
        ○ umount /mnt   解除不了可以用 
        ○ fuser -m   /mnt  看使用该文件系统的进程，杀掉即可解挂
    ● systemctl	http://www.ruanyifeng.com/blog/2016/03/systemd-tutorial-commands.html

    ● 温度管理与gpu降频
        温度过高时gpu频率降低至16/64：
        echo 16 > /sys/bus/platform/drivers/galcore/gpu3DMinclock
        cat /sys/class/thermal/thermal_zone0/temp   //查看当前温度
        echo 25000 > /sys/devices/virtual/thermal/thermal_zone0/trip_point_0_tem
        p    //设置温度阈值
        gputop   //查看当前频率



# FreeRTOS

    在线文档：https://doc.embedfire.com/products/link/zh/latest/tutorial/ebf_freertos_tutorial.html

    任务：数值越大优先级越高，0 代表最低优先级  
    中断：数值越小优先级越高


# 环形缓冲
    https://github.com/barraq/BRBrain/tree/master/firmware

# Python
指令：

	https://pypi.org/ 	#包查找
	https://docs.python.org/zh-cn/3/ 
	pip3 install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple 
    pip  install packname 
	pip  uninstall  packname 
	pip  freeze  	#查看已安装包与版本

pyqt5相关配置：

    pip install PyQt5  
    pip install pyqt5-tools
    
    设置designer.exe
    设置PyUIC
	Parameters写入-m PyQt5.uic.pyuic  $FileName$ -o $FileNameWithoutExtension$.py
	PyQt5信号与槽: https://www.cnblogs.com/Yanjy-OnlyOne/p/12315797.html

xlsx: 

	csv to xlsx：
		import pandas as pd
		csv = pd.read_csv('x.csv', encoding='utf-8') #gbk
		csv.to_excel(x.xlsx, sheet_name='data')
	xlsx to csv:
		xls = pd.read_excel('x.xlsx', index_col=0)
		xls.to_csv('x.csv', encoding='utf-8')
	获取xlsx内容：
		import xlrd
		import numpy as np
		workbook = xlrd.open_workbook(filePath)
		sheet = workbook.sheet_by_index(0)
		row = sheet.nrows
		col = sheet.ncols
		mt = np.zeros([row,col], np.float)
		for i in range(row):
			for j in range(col)
				mt[i][j] = float(sheet.cell(i,j).value)

创建文本并写入内容：

	seq = ['xxx\n']
	with open(fileName, 'w') as f:
		f.writelines(seq)
	



# C++ 
    官网        http://www.cplusplus.com/ 
    现代C++     https://changkun.de/modern-cpp/zh-cn/00-preface/ 
	中文参考手册	https://zh.cppreference.com

    extern "C"  https://blog.csdn.net/u010639500/article/details/87885421
    malloc分析  https://blog.csdn.net/qq_41453285/category_9150569.html
	
	静态成员变量： 类内声明，类外初始化
		class aa{public: static int b;};
		int aa::b = 0;


# SQL

    https://www.w3school.com.cn/sql/index.asp

    mysql -u用户名 -p用户密码
    show databases;	show tables;
    use 库名	 #进入XX库
    desc 表名 ; 	 #查看表结构

    sqlite3  xx.db   #创建新数据库或打开数据库
    .tables    
    .schema    #查看数据库结构
    .schema  表名	  #查看表结构
    .quit 或者 .exit     	#退出

    select * from 表名；  #查看表内容    (* 表示所有字段)
    SELECT COUNT(*) FROM 表名;	   #统计表的行数
    DELETE FROM 表名 WHERE 时间字段 BETWEEN '开始时间' AND '结束时间'；
    INSERT INTO 表名（字段1，2，3） VALUES(值1，2，3)；
    UPDATE 表名 SET A=新值,B=新值;

    判断字段是否为空
    UPDATE xxx_table set run_tim
    e=datetime('now','localtime') WHERE id=3 and run_time is null;

    按某个字段排序
    ORDER BY id LIMIT 0,1
