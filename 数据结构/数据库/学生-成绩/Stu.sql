/*
 Navicat Premium Data Transfer

 Source Server         : SQL Server 2012
 Source Server Type    : SQL Server
 Source Server Version : 11002100
 Source Host           : FANGFANGHUSBAND:1433
 Source Catalog        : School
 Source Schema         : Stu

 Target Server Type    : SQL Server
 Target Server Version : 11002100
 File Encoding         : 65001

 Date: 21/11/2019 01:56:22
*/


-- ----------------------------
-- Table structure for Course
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[Stu].[Course]') AND type IN ('U'))
	DROP TABLE [Stu].[Course]
GO

CREATE TABLE [Stu].[Course] (
  [Cno] int  NOT NULL,
  [Cname] varchar(16) COLLATE Chinese_PRC_CI_AS  NULL,
  [Cpno] int  NULL,
  [Ccredit] int  NULL
)
GO

ALTER TABLE [Stu].[Course] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of [Course]
-- ----------------------------
INSERT INTO [Stu].[Course]  VALUES (N'1', N'数据库', N'5', N'4')
GO

INSERT INTO [Stu].[Course]  VALUES (N'2', N'数学', NULL, N'2')
GO

INSERT INTO [Stu].[Course]  VALUES (N'3', N'信息系统', N'1', N'4')
GO

INSERT INTO [Stu].[Course]  VALUES (N'4', N'操作系统', N'6', N'3')
GO

INSERT INTO [Stu].[Course]  VALUES (N'5', N'数据结构', N'7', N'4')
GO

INSERT INTO [Stu].[Course]  VALUES (N'6', N'数据处理', NULL, N'2')
GO

INSERT INTO [Stu].[Course]  VALUES (N'7', N'PASCAL语言', N'6', N'4')
GO

INSERT INTO [Stu].[Course]  VALUES (N'8', N'DB_Design', NULL, N'3')
GO


-- ----------------------------
-- Table structure for SC
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[Stu].[SC]') AND type IN ('U'))
	DROP TABLE [Stu].[SC]
GO

CREATE TABLE [Stu].[SC] (
  [Sno] varchar(12) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [Cno] int  NOT NULL,
  [Grade] smallint  NULL
)
GO

ALTER TABLE [Stu].[SC] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of [SC]
-- ----------------------------
INSERT INTO [Stu].[SC]  VALUES (N'201215121', N'1', N'92')
GO

INSERT INTO [Stu].[SC]  VALUES (N'201215121', N'2', N'85')
GO

INSERT INTO [Stu].[SC]  VALUES (N'201215121', N'3', N'88')
GO

INSERT INTO [Stu].[SC]  VALUES (N'201215122', N'2', N'90')
GO

INSERT INTO [Stu].[SC]  VALUES (N'201215122', N'3', N'80')
GO

INSERT INTO [Stu].[SC]  VALUES (N'201215123', N'1', NULL)
GO

INSERT INTO [Stu].[SC]  VALUES (N'201215123', N'4', N'55')
GO

INSERT INTO [Stu].[SC]  VALUES (N'316202061007', N'2', N'100')
GO

INSERT INTO [Stu].[SC]  VALUES (N'316202061007', N'6', N'84')
GO


-- ----------------------------
-- Table structure for Student
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[Stu].[Student]') AND type IN ('U'))
	DROP TABLE [Stu].[Student]
GO

CREATE TABLE [Stu].[Student] (
  [Sno] varchar(12) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [Sname] varchar(32) COLLATE Chinese_PRC_CI_AS  NULL,
  [Ssex] varchar(2) COLLATE Chinese_PRC_CI_AS  NULL,
  [Sage] smallint  NULL,
  [Sdept] varchar(16) COLLATE Chinese_PRC_CI_AS  NULL
)
GO

ALTER TABLE [Stu].[Student] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of [Student]
-- ----------------------------
INSERT INTO [Stu].[Student]  VALUES (N'316202061007', N'范天明', N'男', N'21', N'软件工程')
GO

INSERT INTO [Stu].[Student]  VALUES (N'201215121', N'李勇', N'男', N'20', N'CS')
GO

INSERT INTO [Stu].[Student]  VALUES (N'201215122 ', N'刘晨 ', N'女', N'19', N'CS ')
GO

INSERT INTO [Stu].[Student]  VALUES (N'201215123', N'王敏 ', N'女', N'18', N'MA ')
GO

INSERT INTO [Stu].[Student]  VALUES (N'201215125', N'张立', N'男', N'20', N'IS')
GO


-- ----------------------------
-- Indexes structure for table Course
-- ----------------------------
CREATE UNIQUE NONCLUSTERED INDEX [CourCno]
ON [Stu].[Course] (
  [Cno] ASC
)
GO


-- ----------------------------
-- Uniques structure for table Course
-- ----------------------------
ALTER TABLE [Stu].[Course] ADD CONSTRAINT [UQ__Course__9F5E029920C37E59] UNIQUE NONCLUSTERED ([Cname] ASC)
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Primary Key structure for table Course
-- ----------------------------
ALTER TABLE [Stu].[Course] ADD CONSTRAINT [PK__Course__C1FE637343F004B4] PRIMARY KEY CLUSTERED ([Cno])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Indexes structure for table SC
-- ----------------------------
CREATE UNIQUE NONCLUSTERED INDEX [SCsnocno]
ON [Stu].[SC] (
  [Sno] ASC,
  [Cno] DESC
)
GO


-- ----------------------------
-- Primary Key structure for table SC
-- ----------------------------
ALTER TABLE [Stu].[SC] ADD CONSTRAINT [PK__SC__E6000253130DD3FB] PRIMARY KEY CLUSTERED ([Sno], [Cno])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Uniques structure for table Student
-- ----------------------------
ALTER TABLE [Stu].[Student] ADD CONSTRAINT [UQ__Student__52723D275AFE6321] UNIQUE NONCLUSTERED ([Sname] ASC)
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO

ALTER TABLE [Stu].[Student] ADD CONSTRAINT [UQ__Student__CA1FE46539604634] UNIQUE NONCLUSTERED ([Sno] ASC)
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Foreign Keys structure for table Course
-- ----------------------------
ALTER TABLE [Stu].[Course] ADD CONSTRAINT [FK__Course__Cpno__5441852A] FOREIGN KEY ([Cpno]) REFERENCES [Course] ([Cno]) ON DELETE NO ACTION ON UPDATE NO ACTION
GO

