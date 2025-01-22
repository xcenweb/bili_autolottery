-- 启用外键约束
PRAGMA foreign_keys = ON;

-- 转发用户表 (存储抽奖转发号信息)
CREATE TABLE IF NOT EXISTS repost_users (
    uid INTEGER PRIMARY KEY,              -- B站用户ID
    name TEXT NOT NULL,                   -- 用户昵称
    face TEXT,                            -- 用户头像URL
    level INTEGER DEFAULT 0,              -- 用户等级
    status TEXT NOT NULL DEFAULT 'active',-- 用户状态：active(正常)、disabled(已禁用)
    create_time TEXT NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')),
    update_time TEXT NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime'))
);

-- UP主表 (存储抽奖动态发布者信息)
CREATE TABLE IF NOT EXISTS up_users (
    uid INTEGER PRIMARY KEY,              -- UP主ID
    name TEXT NOT NULL,                   -- UP主昵称
    face TEXT,                            -- UP主头像URL
    level INTEGER DEFAULT 0,              -- UP主等级
    is_followed INTEGER DEFAULT 0,        -- 是否已关注：0(未关注)、1(已关注)
    create_time TEXT NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')),
    update_time TEXT NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime'))
);

-- 抽奖动态表
CREATE TABLE IF NOT EXISTS lottery_dynamics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dynamic_id INTEGER UNIQUE NOT NULL,   -- 动态ID
    up_uid INTEGER NOT NULL,              -- UP主ID
    type TEXT NOT NULL,                   -- 抽奖类型：video(视频评论抽奖)、official(官方抽奖工具)、third(第三方抽奖工具)、normal(普通抽奖)
    content TEXT NOT NULL,                -- 动态内容
    description TEXT,                     -- 动态描述/标题
    cover_image TEXT,                     -- 动态封面图
    view_count INTEGER DEFAULT 0,         -- 浏览数
    like_count INTEGER DEFAULT 0,         -- 点赞数
    comment_count INTEGER DEFAULT 0,      -- 评论数
    repost_count INTEGER DEFAULT 0,       -- 转发数
    prizes TEXT,                          -- 奖品信息，JSON格式 [{name: "奖品名", count: 1}, ...]
    conditions TEXT,                      -- 抽奖条件，JSON格式 {follow: true, like: true, comment: true, repost: true}
    require_level INTEGER DEFAULT 0,      -- 参与等级要求
    require_days INTEGER DEFAULT 0,       -- 参与账号注册天数要求
    publish_time TEXT NOT NULL,           -- 发布时间，格式：YYYY-MM-DD HH:MM:SS
    due_time TEXT,                        -- 开奖时间，格式：YYYY-MM-DD HH:MM:SS
    status TEXT NOT NULL DEFAULT 'pending',-- 抽奖状态：pending(等待开奖)、running(抽奖中)、completed(已开奖)、invalid(已失效)
    create_time TEXT NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')),
    update_time TEXT NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')),
    FOREIGN KEY (up_uid) REFERENCES up_users(uid) ON DELETE CASCADE
);

-- 创建索引
CREATE INDEX IF NOT EXISTS idx_lottery_dynamics_status ON lottery_dynamics(status);
CREATE INDEX IF NOT EXISTS idx_lottery_dynamics_due_time ON lottery_dynamics(due_time);
CREATE INDEX IF NOT EXISTS idx_lottery_dynamics_up_uid ON lottery_dynamics(up_uid);
