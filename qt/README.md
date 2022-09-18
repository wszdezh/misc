# Quick

### 高分辨屏自适应处理
#if (QT_VERSION > QT_VERSION_CHECK(5,6,0))
    QGuiApplication::setAttribute(Qt::AA_EnableHighDpiScaling);
    QCoreApplication::setAttribute(Qt::AA_UseHighDpiPixmaps);
#endif

### 非阻塞延时
 QEventLoop loop;
 QTimer::singleShot(msec, &loop, SLOT(quit()));
 loop.exec();

