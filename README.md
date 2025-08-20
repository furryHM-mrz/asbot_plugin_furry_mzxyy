# 趣绮梦云黑查询插件

为 AstrBot 开发的插件，用于查询用户在趣绮梦平台的云黑信息。

## 功能介绍

本插件可以让你在 AstrBot 聊天机器人中通过命令查询用户在趣绮梦平台的云黑记录。插件通过调用趣绮梦云黑API获取并展示用户的详细信息，包括：

- 用户基础信息（手机号、微信、支付宝绑定状态及实名认证情况）
- 用户发送统计（加群数、月活跃数量、累计发送量等）
- 云黑记录（是否被云黑、类型、原因、管理、等级和记录日期）

## 使用方法

在 AstrBot 支持的聊天环境中输入命令：

```
云黑查询 <用户ID>
```

例如：
```
云黑查询 123456
```

机器人会返回该用户在趣绮梦平台的详细信息。

注意：使用此插件需要配置API Key，详情请参考下方安装方式。

## 安装方式

1. 确保你已经安装并运行了 [AstrBot](https://github.com/Soulter/AstrBot)
2. 获取趣绮梦平台的API Key
3. 在 AstrBot 的插件管理界面中添加本插件
4. 在插件配置中填入申请的API Key
5. 或者手动将本插件目录放置在 AstrBot 的插件目录下
6. 重启 AstrBot 以加载插件

## 插件信息

- 插件名称: asbot_plugin_furry-API
- 插件版本: v2.0.0
- 插件作者: furryhm
- 项目仓库: [https://github.com/furryHM-mrz/asbot_plugin_furry_mzxyy](https://github.com/furryHM-mrz/asbot_plugin_furry_mzxyy)

## 语录来源

插件通过调用趣绮梦平台的API获取用户信息，API地址：https://fz.qimeng.fun/OpenAPI/all_f.php

## 开源协议

本项目采用 MIT 协议开源。