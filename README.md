# 创建数据库

## cmd打开终端

```py
# 启动sql服务
net start mysql
mysql -uroot -p
```

## 建立管理员表

```mysql
create table(
	id bigint key,
    username varchar(32),
    password varchar(32)
)
```



