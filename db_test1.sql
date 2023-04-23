-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- 主機: localhost
-- 產生時間： 2023 年 04 月 15 日 02:28
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
-- 資料表結構 `application_list`
--

CREATE TABLE `application_list` (
  `id` int(11) NOT NULL,
  `operator` varchar(42) NOT NULL,
  `licenseId` int(11) NOT NULL,
  `launchId` int(11) NOT NULL,
  `blockNumber` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `application_list`
--

INSERT INTO `application_list` (`id`, `operator`, `licenseId`, `launchId`, `blockNumber`) VALUES
(1, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 0, 0, 7233337),
(2, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 1, 2, 7233379),
(3, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 2, 2, 7233394),
(4, '0x3cBb48D284D1bcE47416011A26E811cFD951cC32', 3, 2, 7233657),
(5, '0x3cBb48D284D1bcE47416011A26E811cFD951cC32', 4, 0, 7233662),
(6, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 5, 3, 7238488),
(7, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 6, 7, 7238489),
(8, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 7, 10, 7238489),
(9, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 8, 12, 7238490),
(10, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 9, 8, 7238490),
(11, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 10, 5, 7238490),
(12, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 11, 9, 7238491),
(13, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 12, 4, 7238491),
(14, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 13, 3, 7238493),
(15, '0x80807B33cc5a24E8003744F0734351d937D52F5E', 14, 3, 7273160),
(16, '0x80807B33cc5a24E8003744F0734351d937D52F5E', 15, 13, 7273168),
(17, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 16, 6, 7279374),
(18, '0x4a85470B95d12BaF29dF93F62FC8F2f12060f567', 17, 3, 7282404),
(19, '0x3cBb48D284D1bcE47416011A26E811cFD951cC32', 18, 3, 7285842),
(20, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 19, 3, 7290312),
(21, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 20, 3, 7290350),
(22, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 21, 3, 7290351),
(23, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 22, 13, 7290353),
(24, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 23, 5, 7290356),
(25, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 24, 0, 7290506),
(26, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 25, 2, 7290507),
(27, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 26, 14, 7294528);

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
(1, '毛怪一號', '雪寶', '毛怪大頭', '毛怪毛怪', '0xe9f5a13658df1a43c6fc7ada0389bcfe38acda0ed0336a1a031828e28ab5b094'),
(2, '毛怪二號', '雪寶', '毛怪側面超級大頭', '毛怪毛怪', '0x29de2eb02f6bef64a173ad6ed5771ca22dc7269da02500cfecd20bc9a3d0bad6'),
(3, '毛怪三號', '雪寶', '毛怪司機', '毛怪', '0x5fa4b856d66c2c5616aeb88b3a603fb22e099179be2470d383df1f9177c3490f'),
(4, '毛怪四號', '雪寶', '毛怪睡覺', '毛怪', '0x9f72f6451b85d905345175fdb0e77b1dfbae6786ec597d23813fde17a7d3d9f5'),
(5, '毛怪五號', '雪寶', '毛怪睡覺偷看', '毛怪', '0xf0b8e62cbc0c0c09616f7669d88c288850a7d46637b6cf2d8d82261b71417a8c'),
(6, '毛怪六號', '雪寶', '毛怪賴床', '毛怪', '0xf724046770249f470f1d72b3bb2ebabde2f19e67ba7281f46506b96c4869ef57'),
(7, '毛怪七號', '雪寶', '毛怪吃飯囉', '毛怪', '0x6607456ce5ea37af5c3a575a352f106d07659493606947edf9fe5e0ffec35cce'),
(8, '毛怪八號', '雪寶', '毛怪怕冷蓋毯子', '毛怪', '0xfc2a6efdda3126e1b335da36985bb72e094312e657d87b031c3747a348995e92'),
(9, '毛怪九號', '雪寶', '毛怪搬新家', '毛怪', '0x377276081423980b1b8ba39c33f477b6bf59d5cca3d8746c91d0a532d2c24620'),
(10, '毛怪十號', '雪寶', '毛怪大頭饋在桌上', '毛怪', '0xebe4bf0ad050052cf5b1e858635651d132bfc82874a870fb4d505793694d76f2'),
(11, '毛怪十一號', '雪寶', '毛怪打擾', '毛怪', '0x3127bbb0573cf515bce3e1a3697a497d3d570eedf8d69c084bccbb077f3ff92f'),
(12, '毛怪十二號', '雪寶', '毛怪新家', '毛怪', '0x99cc7abcc022ebb900739ca6ddac6c46c532a389e03c4dc761cdb3e43ab20c0b'),
(13, '0413', '0413', '0413', '0413', '0x173cf549f553da3bd9fd1c98942c5cb39e6dcd16b65208be4a8ec3420d92edee');

-- --------------------------------------------------------

--
-- 資料表結構 `asset_nft`
--

CREATE TABLE `asset_nft` (
  `NftId` int(11) NOT NULL,
  `sha` varchar(256) NOT NULL,
  `time` int(11) NOT NULL,
  `operator` varchar(42) NOT NULL,
  `transactionHash` varchar(128) NOT NULL,
  `blockNumber` int(11) NOT NULL,
  `img` varchar(128) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `asset_nft`
--

INSERT INTO `asset_nft` (`NftId`, `sha`, `time`, `operator`, `transactionHash`, `blockNumber`, `img`) VALUES
(0, '126fc49c9cb56c11daf88beafa031c00992d65cc352721a0c526b1e1d196d7bf', 1680462874, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', '0xe9f5a13658df1a43c6fc7ada0389bcfe38acda0ed0336a1a031828e28ab5b094', 7233240, 'https://blockchain-omekas.dlll.nccu.edu.tw/files/square/8a09def1bfc29be99355d60f1ac4f566fb695d79.jpg'),
(1, 'fb1ecb096e65be675cf8e44d874037c6bc665e2e3adcba8299f00ac9b08f292e', 1680463084, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', '0x29de2eb02f6bef64a173ad6ed5771ca22dc7269da02500cfecd20bc9a3d0bad6', 7233254, 'https://blockchain-omekas.dlll.nccu.edu.tw/files/square/9f398148ea3c0a1cc95caabdbccaef443dbf85ff.jpg'),
(2, '621fdbd5f6937bd0169598a8eaa163e4ace372cd61e0259fc9a44f637dece8c5', 1680535519, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', '0x5fa4b856d66c2c5616aeb88b3a603fb22e099179be2470d383df1f9177c3490f', 7238083, 'https://blockchain-omekas.dlll.nccu.edu.tw/files/square/4235a10631d86c07ee87dfaa14cfc8ce07c97a4e.jpg'),
(3, 'be6b8c7643f063e2d5efb5f2e7f2db56f75cc8a6f62fe50f2e4f885b4061c33d', 1680536944, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', '0x9f72f6451b85d905345175fdb0e77b1dfbae6786ec597d23813fde17a7d3d9f5', 7238178, 'https://blockchain-omekas.dlll.nccu.edu.tw/files/square/fa61dc668a5e27f67374baadb6668cc65b221e7e.jpg'),
(4, 'e04d5c49a0a9a35d66c152843df8fc2559e71573abd9c5c33f95560b1d4d1ae8', 1680537139, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', '0xf0b8e62cbc0c0c09616f7669d88c288850a7d46637b6cf2d8d82261b71417a8c', 7238191, 'https://blockchain-omekas.dlll.nccu.edu.tw/files/square/21b140e621c9247b6a8fa5f24e9391a791aeddf8.jpg'),
(5, 'e7b924231c6b95d8dd42379830376e73ad7bc1afed36195e3efa9f6dc6dbad99', 1680537469, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', '0xf724046770249f470f1d72b3bb2ebabde2f19e67ba7281f46506b96c4869ef57', 7238213, 'https://blockchain-omekas.dlll.nccu.edu.tw/files/square/c90164d761f94d28879870267d04c1c4531496e5.jpg'),
(6, 'afd64bde7c7e7f79f14a3a4b984fac51867187d80dfb1c2cd0a872002aeab188', 1680538234, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', '0x6607456ce5ea37af5c3a575a352f106d07659493606947edf9fe5e0ffec35cce', 7238264, 'https://blockchain-omekas.dlll.nccu.edu.tw/files/square/8eb2b2ce339e4a6c3f9f64dab6903f030947896b.jpg'),
(7, 'e34204f720d3b0d99c32380fa5f592e0288d1a24b203f1d0e3a254c92547fa17', 1680538519, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', '0xfc2a6efdda3126e1b335da36985bb72e094312e657d87b031c3747a348995e92', 7238283, 'https://blockchain-omekas.dlll.nccu.edu.tw/files/square/b11db44ad7f60e1d6f5127dffe7edb5457c37fbb.jpg'),
(8, 'a8baf1f61582823775af2ed68355db8da47bcfc3b4079d2cf7ff84bde1285281', 1680538699, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', '0x377276081423980b1b8ba39c33f477b6bf59d5cca3d8746c91d0a532d2c24620', 7238295, 'https://blockchain-omekas.dlll.nccu.edu.tw/files/square/de2b16b238457ce0248602ab6b52407ceab609a6.jpg'),
(9, 'c0a8abf2142938947f5bc031a46b41e075a46bba28689997336331bc802a789d', 1680538969, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', '0xebe4bf0ad050052cf5b1e858635651d132bfc82874a870fb4d505793694d76f2', 7238313, 'https://blockchain-omekas.dlll.nccu.edu.tw/files/square/fccc7b24fe4358150a6701e6ed328418390c82ea.jpg'),
(10, '126fc49c9cb56c11daf88beafa031c00992d65cc352721a0c526b1e1d196d7bf', 1680539449, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', '0x3127bbb0573cf515bce3e1a3697a497d3d570eedf8d69c084bccbb077f3ff92f', 7238345, 'https://blockchain-omekas.dlll.nccu.edu.tw/files/square/492aa869359c6d506bab06bef924857e4ca861ad.jpg'),
(11, 'a8baf1f61582823775af2ed68355db8da47bcfc3b4079d2cf7ff84bde1285281', 1680539494, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', '0x99cc7abcc022ebb900739ca6ddac6c46c532a389e03c4dc761cdb3e43ab20c0b', 7238348, 'https://blockchain-omekas.dlll.nccu.edu.tw/files/square/03b40ba1d74bede3fd8abf7fd6fa0ccab5810f13.jpg'),
(12, 'e34204f720d3b0d99c32380fa5f592e0288d1a24b203f1d0e3a254c92547fa17', 1681381939, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', '0x173cf549f553da3bd9fd1c98942c5cb39e6dcd16b65208be4a8ec3420d92edee', 7294511, 'https://blockchain-omekas.dlll.nccu.edu.tw/files/square/b056ba70122420a4e8975a4c4e5b9063a9740728.jpg');

-- --------------------------------------------------------

--
-- 資料表結構 `interact`
--

CREATE TABLE `interact` (
  `id` int(11) NOT NULL,
  `address` varchar(42) NOT NULL,
  `target` varchar(128) NOT NULL,
  `interact` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `interact`
--

INSERT INTO `interact` (`id`, `address`, `target`, `interact`) VALUES
(1, 'my_address', 'https://blockchain-omekas.dlll.nccu.edu.tw/files/square/8bb9535b165b7cffe3cf2ea0a4f15cf61d1f1cda.jpg', '0'),
(2, 'my_address', 'https://blockchain-omekas.dlll.nccu.edu.tw/files/square/8bb9535b165b7cffe3cf2ea0a4f15cf61d1f1cda.jpg', '1'),
(3, 'my_address', 'http://blockchain-omekas.ccstw.nccu.edu.tw/files/square/ce50c61b02d45bc06892764f2272419a211f67c7.jpg', '1'),
(4, 'my_address', 'http://blockchain-omekas.ccstw.nccu.edu.tw/files/square/ce50c61b02d45bc06892764f2272419a211f67c7.jpg', '0'),
(5, 'my_address', 'http://blockchain-omekas.ccstw.nccu.edu.tw/files/square/ce50c61b02d45bc06892764f2272419a211f67c7.jpg', '0'),
(6, 'my_address', 'https://dev-partyisland.dlll.nccu.edu.tw/exhibition?id=6422a266ff11675afdb2f0bf&room=1&watchType=preview', '1'),
(7, 'my_address', 'https://dev-partyisland.dlll.nccu.edu.tw/exhibition?id=6422a266ff11675afdb2f0bf&room=1&watchType=preview', '1'),
(8, 'my_address', 'https://dev-partyisland.dlll.nccu.edu.tw/exhibition?id=6422a266ff11675afdb2f0bf&room=1&watchType=preview', '1'),
(9, 'my_address', 'https://dev-partyisland.dlll.nccu.edu.tw/exhibition?id=6432efeee4f62d857f1536e3&room=1', '1'),
(10, 'my_address', 'https://dev-partyisland.dlll.nccu.edu.tw/exhibition?id=641d4294ff11675afdb2ebaf&room=1', '0'),
(11, 'my_address', 'https://dev-partyisland.dlll.nccu.edu.tw/exhibition?id=641d4294ff11675afdb2ebaf&room=1', '0'),
(12, 'my_address', 'https://dev-partyisland.dlll.nccu.edu.tw/exhibition?id=6432efeee4f62d857f1536e3&room=1', '1'),
(13, 'my_address', 'https://blockchain-omekas.dlll.nccu.edu.tw/files/large/b056ba70122420a4e8975a4c4e5b9063a9740728.jpg', '1'),
(14, 'my_address', 'https://blockchain-omekas.dlll.nccu.edu.tw/files/large/b056ba70122420a4e8975a4c4e5b9063a9740728.jpg', '1'),
(15, 'my_address', 'https://blockchain-omekas.dlll.nccu.edu.tw/files/large/b056ba70122420a4e8975a4c4e5b9063a9740728.jpg', '0'),
(16, 'my_address', 'https://blockchain-omekas.dlll.nccu.edu.tw/files/large/b056ba70122420a4e8975a4c4e5b9063a9740728.jpg', '1'),
(17, 'my_address', 'https://blockchain-omekas.dlll.nccu.edu.tw/files/large/b056ba70122420a4e8975a4c4e5b9063a9740728.jpg', '0'),
(18, 'my_address', 'https://blockchain-omekas.dlll.nccu.edu.tw/files/large/b056ba70122420a4e8975a4c4e5b9063a9740728.jpg', '0'),
(19, 'my_address', 'https://blockchain-omekas.dlll.nccu.edu.tw/files/large/b056ba70122420a4e8975a4c4e5b9063a9740728.jpg', '0');

-- --------------------------------------------------------

--
-- 資料表結構 `launch_count`
--

CREATE TABLE `launch_count` (
  `launch_id` int(11) NOT NULL,
  `operator` varchar(42) NOT NULL,
  `status` tinyint(4) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `launch_detail`
--

CREATE TABLE `launch_detail` (
  `launch_id` int(11) NOT NULL,
  `token_id` int(11) NOT NULL,
  `asset_title` varchar(64) NOT NULL,
  `rent_days` int(11) NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `launch_to_nft`
--

CREATE TABLE `launch_to_nft` (
  `launch_id` int(11) NOT NULL,
  `tokenId` int(11) NOT NULL COMMENT 'tokenId (+1)',
  `operator` varchar(42) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `blockNumber` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `launch_to_nft`
--

INSERT INTO `launch_to_nft` (`launch_id`, `tokenId`, `operator`, `status`, `blockNumber`) VALUES
(0, 0, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 1, 7233274),
(1, 1, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 0, 7233283),
(2, 1, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 1, 7233309),
(3, 2, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 1, 7238404),
(4, 3, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 1, 7238409),
(5, 4, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 1, 7238431),
(6, 5, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 1, 7238433),
(7, 6, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 1, 7238435),
(8, 7, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 1, 7238436),
(9, 8, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 1, 7238437),
(10, 9, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 1, 7238479),
(11, 10, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 0, 7238481),
(12, 11, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 1, 7238481),
(13, 2, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 1, 7273166),
(14, 12, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 1, 7294519);

-- --------------------------------------------------------

--
-- 資料表結構 `pi_user`
--

CREATE TABLE `pi_user` (
  `id` int(11) NOT NULL,
  `nickname` varchar(256) NOT NULL,
  `account` varchar(256) NOT NULL,
  `password` varchar(256) NOT NULL,
  `token` varchar(512) NOT NULL,
  `_id` varchar(128) DEFAULT NULL,
  `email` varchar(128) DEFAULT NULL,
  `address` varchar(42) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `pi_user`
--

INSERT INTO `pi_user` (`id`, `nickname`, `account`, `password`, `token`, `_id`, `email`, `address`) VALUES
(1, 'aaa', 'aaa', 'aaa', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NDI3YmM1Y2U0ZjYyZDg1N2YwZTY5M2YiLCJhY2NvdW50IjoiYWFhIiwidHlwZSI6InNlbGxlciIsImV4cCI6MTY4MjAxNzcxNi4yMjYsImlhdCI6MTY4MTQxMjkxNn0.5L4uVBhv6nRJsUkc3aEnSiRrmjBlrLfs8O55EKFWFq4', '6427bc5ce4f62d857f0e693f', 'aa@aa.aa', '0x3cBb48D284D1bcE47416011A26E811cFD951cC32'),
(2, 'bbbb', 'bbbb', 'bbbb', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NDI3YzU2YmU0ZjYyZDg1N2YwZTY5NjQiLCJhY2NvdW50IjoiYmJiYiIsInR5cGUiOiJub3JtYWwiLCJleHAiOjE2ODE4NDg2ODUuMjg2LCJpYXQiOjE2ODEyNDM4ODV9.aHq67uTxMsCz9Mpxz-GRepeV1ctsClUxYSmNL5MYUUM', '6427c56be4f62d857f0e6964', 'bbb@bb.bb', '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727'),
(3, 'cccc', 'cccc', 'cccc', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NDI3Y2E1NGU0ZjYyZDg1N2YwZTY5ODMiLCJhY2NvdW50IjoiY2NjYyIsInR5cGUiOiJub3JtYWwiLCJleHAiOjE2ODE2ODA1MzUuNzM2LCJpYXQiOjE2ODEwNzU3MzV9.qVFDep_yXl6ky5nh80a12TBGaWSTvxDnLHWMOzi0Yas', '6427ca54e4f62d857f0e6983', 'cccc@cc.cc', '0x80807B33cc5a24E8003744F0734351d937D52F5E'),
(4, 'tyu', 'yucheng', '', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NDEwMTkxYjI2ZWQwMjQwZjUyN2JjMGEiLCJhY2NvdW50IjoieXVjaGVuZyIsInR5cGUiOiJzZWxsZXIiLCJleHAiOjE2ODIxMDEzNDkuOTA1LCJpYXQiOjE2ODE0OTY1NDl9.Z45s1F26lhfwd_7HT3r8m2p6pIzIT1K7u1V9JAW-SqQ', '6410191b26ed0240f527bc0a', 'zeng3355755@gmail.com', '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727'),
(5, 'dddd', 'dddd', 'dddd', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NDI3ZWIxY2U0ZjYyZDg1N2YwZTZhODMiLCJhY2NvdW50IjoiZGRkZCIsInR5cGUiOiJub3JtYWwiLCJleHAiOjE2ODE4NDM1NTUuNDc2LCJpYXQiOjE2ODEyMzg3NTV9.t6Zz3ZNyga0FTKbB-HYPtlRZm3w2tYKcFjizz4MvoxQ', '6427eb1ce4f62d857f0e6a83', 'dddd@dd.dd', '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727'),
(6, 'qwer', 'qwer', '', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NDIxNDA1M2ZmMTE2NzVhZmRiMmYwMTQiLCJhY2NvdW50IjoicXdlciIsInR5cGUiOiJzZWxsZXIiLCJleHAiOjE2ODIwNjcxNTIuNDM1LCJpYXQiOjE2ODE0NjIzNTJ9.rK4Os2f29oeiwLzreaEmBrohmVhpEGEIgyTbRTcvqVU', '64214053ff11675afdb2f014', 'qwer@qwer.qq', '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727'),
(7, 'test2', 'test2', '', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2M2JiOTBjZjVhY2U3MjAzMmIwYjU5NjIiLCJhY2NvdW50IjoidGVzdDIiLCJ0eXBlIjoic2VsbGVyIiwiZXhwIjoxNjgxODA0OTM1LjE5NSwiaWF0IjoxNjgxMjAwMTM1fQ.MjIS9hVviV4opDLsuRrfllwxDwye1IYA3AhQ_sEWLug', '63bb90cf5ace72032b0b5962', 'test2@dlll.nccu.edu.tw', '0x4a85470B95d12BaF29dF93F62FC8F2f12060f567'),
(8, 'zxcv', 'zxcv', 'zxcv', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NDM1YWM3MzE4Mzk1MDAxYzMyM2NmODMiLCJhY2NvdW50IjoienhjdiIsInR5cGUiOiJub3JtYWwiLCJleHAiOjE2ODE4NDg1NDMuNTAzLCJpYXQiOjE2ODEyNDM3NDN9.fkqMOKGDb5eiMLXXSOVPaYhGNyXq72yw1tfa0Gleh5E', '6435ac7318395001c323cf83', 'zxcv@zxcv.zx', '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727');

-- --------------------------------------------------------

--
-- 資料表結構 `revenue`
--

CREATE TABLE `revenue` (
  `address` varchar(42) NOT NULL,
  `revenue` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `room_list`
--

CREATE TABLE `room_list` (
  `id` int(11) NOT NULL,
  `room_id` varchar(64) NOT NULL,
  `coverUrl` varchar(128) DEFAULT NULL,
  `signboardUrl` varchar(128) DEFAULT NULL,
  `title` varchar(64) DEFAULT NULL,
  `introduction` varchar(256) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `room_list`
--

INSERT INTO `room_list` (`id`, `room_id`, `coverUrl`, `signboardUrl`, `title`, `introduction`) VALUES
(1, '6423ea3bff11675afdb2f62c', '', '', 'zxcv', ''),
(2, '6423e0e3ff11675afdb2f545', '', '', 'asdf', ''),
(3, '6422a266ff11675afdb2f0bf', '', '', 'qwer', ''),
(4, '641d4294ff11675afdb2ebaf', 'https://dev-partyisland.dlll.nccu.edu.tw/upload/exhibitionCovers/UTo6nGHYY.png', 'https://dev-partyisland.dlll.nccu.edu.tw/upload/exhibitionSignboards/HIoaNP4JE.png', 'FirstRoom1', ''),
(5, '63ed99a86f27f315061751e8', 'https://dev-partyisland.dlll.nccu.edu.tw/upload/exhibitionCovers/EW15ym7P2.png', 'https://dev-partyisland.dlll.nccu.edu.tw/upload/exhibitionSignboards/uoOBj4hx5.png', 'test5', '9987999'),
(6, '63bb91085ace72032b0b5976', 'https://dev-partyisland.dlll.nccu.edu.tw/upload/exhibitionCovers/l9qZ_yoQf.jpeg', 'https://dev-partyisland.dlll.nccu.edu.tw/upload/exhibitionSignboards/8deIgl2Kp.png', '789', '123123'),
(7, '63aa95fccf5b702af42f8165', 'http://partyisland.dlll.nccu.edu.tw/upload/exhibitionCovers/pJwSEMUvL.jpeg', 'http://partyisland.dlll.nccu.edu.tw/upload/exhibitionSignboards/X1eHJp_r4.jpeg', '1st view point', ''),
(8, '63a90a1acf5b702af42f7994', 'http://partyisland.dlll.nccu.edu.tw/upload/exhibitionCovers/hzhYdqfo0.jpeg', 'http://partyisland.dlll.nccu.edu.tw/upload/exhibitionSignboards/Lcf8oAXEP.jpeg', 'TEST', '第三人稱視角（看到被害者）'),
(9, '6347bcec06311b05797db137', 'http://partyisland.dlll.nccu.edu.tw/upload/exhibitionCovers/QoUqV4SDK.jpeg', 'http://partyisland.dlll.nccu.edu.tw/upload/exhibitionSignboards/nmqdJL9ny.jpeg', 'test2', ''),
(10, '6347b20106311b05797db06d', 'http://partyisland.dlll.nccu.edu.tw/upload/exhibitionCovers/mPxzFw9z_.jpeg', 'http://partyisland.dlll.nccu.edu.tw/upload/exhibitionSignboards/azNkC8QsL.jpeg', 'test', ''),
(11, '6432efeee4f62d857f1536e3', '', '', 'A1', ''),
(12, '6435224e18395001c320e66b', '', '', 'yu3', ''),
(13, '6435e7ef18395001c32511a5', '', '', 'A2', ''),
(14, '6429f061e4f62d857f0e7437', '', '', 'b', '');

-- --------------------------------------------------------

--
-- 資料表結構 `set_room`
--

CREATE TABLE `set_room` (
  `id` int(11) NOT NULL,
  `address` varchar(42) DEFAULT NULL COMMENT 'Room Owner',
  `room_id` varchar(64) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `blockNumber` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `set_room`
--

INSERT INTO `set_room` (`id`, `address`, `room_id`, `price`, `blockNumber`) VALUES
(2, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', '6422a266ff11675afdb2f0bf', 50, 7265753),
(3, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', '641d4294ff11675afdb2ebaf', 300, 7280165),
(5, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', '6429f061e4f62d857f0e7437', 100, 7294537),
(6, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', '6423e0e3ff11675afdb2f545', 200, 7264813),
(7, '0x', '6423ea3bff11675afdb2f62c', 0, 0),
(8, '0x80807B33cc5a24E8003744F0734351d937D52F5E', '6432efeee4f62d857f1536e3', 100, 7273093),
(9, '0x4a85470B95d12BaF29dF93F62FC8F2f12060f567', '63bb91085ace72032b0b5976', 10, 7282461),
(10, '0x', '63ed99a86f27f315061751e8', 0, 0),
(11, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', '6435224e18395001c320e66b', 10, 7282639),
(12, '0x3cBb48D284D1bcE47416011A26E811cFD951cC32', '6435e7ef18395001c32511a5', 150, 7286040);

-- --------------------------------------------------------

--
-- 資料表結構 `ticket`
--

CREATE TABLE `ticket` (
  `id` int(11) NOT NULL,
  `address` varchar(42) NOT NULL COMMENT 'ticket owner',
  `ticket_id` int(11) NOT NULL,
  `room_id` varchar(64) NOT NULL,
  `blockNumber` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `ticket`
--

INSERT INTO `ticket` (`id`, `address`, `ticket_id`, `room_id`, `blockNumber`) VALUES
(1, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 0, '641d4294ff11675afdb2ebaf', 7266538),
(2, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 1, '6432efeee4f62d857f1536e3', 7273171),
(3, '0x80807B33cc5a24E8003744F0734351d937D52F5E', 2, '641d4294ff11675afdb2ebaf', 7273180),
(4, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 3, '63bb91085ace72032b0b5976', 7282464),
(5, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 4, '6422a266ff11675afdb2f0bf', 7282494),
(6, '0x3cBb48D284D1bcE47416011A26E811cFD951cC32', 5, '6432efeee4f62d857f1536e3', 7285845),
(7, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 6, '6429f061e4f62d857f0e7437', 7294553),
(8, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 7, '6423e0e3ff11675afdb2f545', 7299926),
(9, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 8, '6423e0e3ff11675afdb2f545', 7299931);

-- --------------------------------------------------------

--
-- 資料表結構 `token`
--

CREATE TABLE `token` (
  `id` int(11) NOT NULL,
  `token_tokenId` int(11) DEFAULT NULL,
  `owner` varchar(42) DEFAULT NULL COMMENT 'token_to',
  `status` tinyint(1) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='Token status and owner';

-- --------------------------------------------------------

--
-- 資料表結構 `transfer`
--

CREATE TABLE `transfer` (
  `id` int(11) NOT NULL,
  `token_from` varchar(42) NOT NULL,
  `token_to` varchar(42) NOT NULL,
  `token_tokenId` int(11) NOT NULL,
  `token_transactionHash` varchar(66) NOT NULL,
  `token_blockNumber` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `address` varchar(42) NOT NULL,
  `email` varchar(128) NOT NULL,
  `name` varchar(128) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `activated` tinyint(1) NOT NULL,
  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `user`
--

INSERT INTO `user` (`id`, `address`, `email`, `name`, `status`, `activated`, `created`, `modified`) VALUES
(1, '0xe0d2fd7B0F8a4e1D1f5Ecc9c6Bc9Fa51a1B6B727', 'zeng3355755@gmail.com', 'tyu', 1, 1, '2022-09-18 17:01:18', '2022-09-18 17:01:18'),
(2, '0x3cBb48D284D1bcE47416011A26E811cFD951cC32', '000@000.00', '00', 1, 0, '2022-10-03 07:36:08', '2022-10-03 07:36:08');

-- --------------------------------------------------------

--
-- 資料表結構 `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` char(40) NOT NULL,
  `name` varchar(128) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `users`
--

INSERT INTO `users` (`id`, `email`, `password`, `name`) VALUES
(1, 'zeng3355755@gmail.com', 'bb9fdc0778eba3760f3d73b7e8bb27c41bb2186c', 'tyu');

--
-- 已匯出資料表的索引
--

--
-- 資料表索引 `application_list`
--
ALTER TABLE `application_list`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `asset_detail`
--
ALTER TABLE `asset_detail`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `asset_nft`
--
ALTER TABLE `asset_nft`
  ADD PRIMARY KEY (`NftId`);

--
-- 資料表索引 `interact`
--
ALTER TABLE `interact`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `pi_user`
--
ALTER TABLE `pi_user`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `room_list`
--
ALTER TABLE `room_list`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `set_room`
--
ALTER TABLE `set_room`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `ticket`
--
ALTER TABLE `ticket`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `token`
--
ALTER TABLE `token`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `transfer`
--
ALTER TABLE `transfer`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- 在匯出的資料表使用 AUTO_INCREMENT
--

--
-- 使用資料表 AUTO_INCREMENT `application_list`
--
ALTER TABLE `application_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
--
-- 使用資料表 AUTO_INCREMENT `asset_detail`
--
ALTER TABLE `asset_detail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- 使用資料表 AUTO_INCREMENT `interact`
--
ALTER TABLE `interact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
--
-- 使用資料表 AUTO_INCREMENT `pi_user`
--
ALTER TABLE `pi_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- 使用資料表 AUTO_INCREMENT `room_list`
--
ALTER TABLE `room_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- 使用資料表 AUTO_INCREMENT `set_room`
--
ALTER TABLE `set_room`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- 使用資料表 AUTO_INCREMENT `ticket`
--
ALTER TABLE `ticket`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- 使用資料表 AUTO_INCREMENT `token`
--
ALTER TABLE `token`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用資料表 AUTO_INCREMENT `transfer`
--
ALTER TABLE `transfer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用資料表 AUTO_INCREMENT `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- 使用資料表 AUTO_INCREMENT `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
