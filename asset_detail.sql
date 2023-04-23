-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- 主機: localhost
-- 產生時間： 2023 年 03 月 06 日 15:24
-- 伺服器版本: 5.7.27-0ubuntu0.16.04.1-log
-- PHP 版本： 7.2.22-1+ubuntu16.04.1+deb.sury.org+1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `db_test1`
--

-- --------------------------------------------------------

--
-- 資料表結構 `asset_detail`
--

CREATE TABLE `asset_detail` (
  `id` int(11) NOT NULL,
  `title` varchar(64) NOT NULL,
  `creator` varchar(64) NOT NULL,
  `description` text NOT NULL,
  `subject` varchar(64) NOT NULL,
  `transactionHash` varchar(128) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `asset_detail`
--

INSERT INTO `asset_detail` (`id`, `title`, `creator`, `description`, `subject`, `transactionHash`) VALUES
(1, '測試測試', 'yucheng', '0', '', '0x112be5f762cc1f4722eaac80758911099a4d271ddda40bdb9afd017be12df532'),
(2, '月亮', 'tyu', 'moon', '', '0x55b2517dd956a272f929808bd41f30ece9c9969f9abd6170518d0ed9d5f4ff3c'),
(3, '白宮', '要畢業的人', '遊戲畫面', '', '0x5035d06548c128b528e4fdaf61deac9845129e1a3c2a8f8f14df3fb5dafc810a'),
(4, '十二門徒石', 'yucheng', '澳洲大洋路', '', '0xd6d5e8b97f0b7a174d528e99616a69ae4869b271cca459b13dbc83bfdd704691'),
(5, '系統自拍', 'YuCheng', '成功自拍', '', '0x825b0e178445252569e14fbad9d8a4110a4539298b87a9fc8ce196f081461566'),
(6, '手機上傳', '我的手機', '沒有描述', '', ''),
(7, '0302', 'yucheng', '123', '', '0x1cf5f665069013388478813f06376201a9988169e687133eba6799a6e52d23dd'),
(8, 'qaz', 'qaz', 'qaz', '', '0x2df5e7c153eab6eee816b6296ef1a3f73c2948dcb07933a770f7d8b490cc5522'),
(9, 'ㄇ', 'ㄇ', 'ㄇ', '', '0xbefe6773c1a8c539b9cb08ab6d02b05ec5f5081964e9c468bd4ea78c9d34df0b'),
(10, '標題', '創建者', '描述', '類別', '0xb665abcd064559993f8e6978c9bb80b07257dad9b4a98e3242bf99fbf73119fd'),
(11, '標題三', '創建者三', '描述三', '類別三', '0x2376a0e5248056b4c623295baa6a456dc4f5f89ec857de68276a27b85ffb02e2'),
(12, '0306標題', '0306創建者', '0306描述', '0306主題', '0x4e36e085816faf508c88282e71c60434ddba0392113e3e6a94fbf7e604d4fb06');

--
-- 已匯出資料表的索引
--

--
-- 資料表索引 `asset_detail`
--
ALTER TABLE `asset_detail`
  ADD PRIMARY KEY (`id`);

--
-- 在匯出的資料表使用 AUTO_INCREMENT
--

--
-- 使用資料表 AUTO_INCREMENT `asset_detail`
--
ALTER TABLE `asset_detail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
