# Linux
    ● grep -nr "xxxxx" /etc/ 或 grep -E 'k1|k2'
    ● find /etc/ -name rc.local
    ● du -hd 1   查看一级目录大小
    ● chown -R wangshize:wangshize /filename     递归修改文件所属
    ● ln -sf  目标名  软连接名
    ● cat /proc/cmdline   可以看bootargs
    ● ps -T pid 查看线程
    ● lsof  看进程打开的文件描述符
    ● cat /dev/null > xxx  清空文件
    ● top -H -p pid  查看线程
    ● ! number 执行第几条历史命令， echo $?  看上一条命令返回值
    ● su 切换用户（没写用户默认root）， sudo 提升权限
    ● telnet  *.*.*.* portnum   只能用于测试TCP端口
    ● vim 16进制编辑:1. %!xxd  2. %!xxd   3. wq
    ● 命令1 && 命令2 || 命令3   :前一条执行成功才执行第二条，否则执行命令3
        命令1;  命令2   :不管前一条执行是否成功，都会执行第二条
    ● ldd xxx  查看库依赖
    ● crontab时间计算 crontab.guru
    ● 阿里镜像  https://developer.aliyun.com/mirror/?serviceType=mirror
    ● while true;do cmd1;cmd2;done
    
    ● make
        make VERBOSE=1 #输出编译过程

    ● 烧写uboot
        echo 0 > /sys/block/mmcblk1boot0/force_ro
        dd if=uboot.imx  of=/dev/mmcblk1boot0  bs=1  seek=1024

    ● 终端直接向串口发送数据
        ○ stty -F /dev/ttymxc1
        ○ stty -F /dev/ttyS1 speed 115200
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

    ● 温度管理与gpu降频
        温度过高时gpu频率降低至16/64：
        echo 16 > /sys/bus/platform/drivers/galcore/gpu3DMinClock
        cat /sys/class/thermal/thermal_zone0/temp   //查看当前温度
        echo 25000 > /sys/devices/virtual/thermal/thermal_zone0/trip_point_0_temp    //设置温度阈值
        gputop   //查看当前频率

    ● cmake
        https://blog.csdn.net/zhizhengguan/article/details/107034372

    ● GDB
        容器打印 https://gist.githubusercontent.com/skyscribe/3978082/raw/9ec52a76f6793ac9ad12fae11c10db458b64e79b/.gdbinit
        100个gdb小技巧 https://github.com/hellogcc/100-gdb-tips
        https://www.cnblogs.com/lizhimin123/p/10416975.html

    ● FreeRTOS
        在线文档：https://doc.embedfire.com/products/link/zh/latest/tutorial/ebf_freertos_tutorial.html

# C++ 
    官网 http://www.cplusplus.com/ 
    现代C++ https://changkun.de/modern-cpp/zh-cn/00-preface/ 
    中文参考手册 https://zh.cppreference.com
    在线编译 http://cpp.sh/

    extern "C"  https://www.cnblogs.com/TenosDoIt/p/3163621.html
    malloc分析  https://blog.csdn.net/qq_41453285/category_9150569.html
    编译优化 https://tech.meituan.com/2020/12/10/apache-kylin-practice-in-meituan.html
    
    1. 静态成员变量： 类内声明，类外初始化
        class aa{public: static int b;};
        int aa::b = 0;
    2. 用时计算
        #include <chrono>
        auto start = std::chrono::steady_clock::now();
        // xxxx
        auto end = std::chrono::steady_clock::now();
        std::cout << "elapsed time: " << std::chrono::duration<double>(end-start).count() << "s\n";
    3. 前置类型声明，避免头文件的引入，优化编译：只能用于指针、引用、函数
    4.
    5. 
# QT 
    1. 非阻塞延时
        QEventLoop loop;
        QTimer::singleShot(msec, &loop, SLOT(quit()));
        loop.exec();
    2. 数据容器 https://qtguide.ustclug.org
    3. 单例 Q_GLOBAL_STATIC(QThreadPool, theInstance)  用法看qthreadpool.h
    4. QML单例：QT助手 qmlRegisterSingletonType
    5. Inside Qt https://blog.csdn.net/ACK_ACK/article/details/104729945/
    6、QML
        a. font.family: "Microsoft YaHei"
        b. Qt.formatDateTime(new Date(), "yyyy-MM-dd HH:mm:ss.zzz")

# Python

    Python资源大全 http://jobbole.github.io/awesome-python-cn/
    https://pypi.org/ 	#包查找
    https://docs.python.org/zh-cn/3/

    指令:
	  pip3 install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple 
	  pip  install packname 
	  pip  uninstall  packname 
	  pip  freeze  	#查看已安装包与版本
	  pyinstaller -F -w --icon="图标绝对路径" name.py   打包为单个exe
	  pyinstaller -D -w --icon="图标绝对路径" name.py   打包为单个文件夹
	  打包第三方资源，编译后在xx.spec修改 datas=[("aes_encrypt.exe",".")]


# Anaconda

	创建环境： conda create -n xxxx python=3.8.5
	删除环境： conda remove -n xxxx --all
	查看环境： conda env list  或  conda info --envs
	切换环境： activate xxx
	查看环境中的包： conda list
	查看当前源：conda config --show-sources
	切换源：
		https://blog.csdn.net/qq_29007291/article/details/81103603
	安装指定版本tensorflow：
		conda install --channel 
		https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/win-64  tensorflow=1.14
	或 
		pip3 install tensorflow -i https://pypi.tuna.tsinghua.edu.cn/simple

