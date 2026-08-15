-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 30, 2019 at 02:08 PM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ims`
--

-- --------------------------------------------------------

--
-- Stand-in structure for view `available_stock`
-- (See below for the actual view)
--
CREATE TABLE `available_stock` (
`supp_name` varchar(50)
,`item_id` int(20)
,`item_name` varchar(100)
,`category_name` varchar(50)
,`brand_name` varchar(50)
,`stock_quantity` int(20)
);

-- --------------------------------------------------------

--
-- Table structure for table `billing`
--

CREATE TABLE `billing` (
  `billing_id` int(20) NOT NULL,
  `billing_customer_id` int(20) NOT NULL,
  `billing_datetime` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `billing`
--

INSERT INTO `billing` (`billing_id`, `billing_customer_id`, `billing_datetime`) VALUES
(1, 1, '2018-12-23 13:26:20'),
(2, 3, '2018-12-23 13:26:57'),
(3, 2, '2018-12-23 13:27:17'),
(4, 1, '2018-12-23 21:30:09'),
(5, 6, '2019-04-30 17:17:03');

-- --------------------------------------------------------

--
-- Table structure for table `brand`
--

CREATE TABLE `brand` (
  `brand_id` int(20) NOT NULL,
  `brand_name` varchar(50) NOT NULL DEFAULT 'No Brand'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `brand`
--

INSERT INTO `brand` (`brand_id`, `brand_name`) VALUES
(1, 'Asian Paints'),
(2, 'Ultratech'),
(3, 'Greenply'),
(4, 'Dupli'),
(5, '--Not Selected--'),
(6, 'lalala'),
(7, 'kkhjk');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `category_id` int(20) NOT NULL,
  `category_name` varchar(50) NOT NULL DEFAULT 'No Category'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`category_id`, `category_name`) VALUES
(1, 'Paint'),
(2, 'Plywood'),
(3, 'fgh'),
(4, '--Not Selected--');

-- --------------------------------------------------------

--
-- Table structure for table `customer_info`
--

CREATE TABLE `customer_info` (
  `C_id` int(20) NOT NULL,
  `C_name` varchar(100) DEFAULT 'Anonymous',
  `C_contact` bigint(15) NOT NULL,
  `C_address` varchar(100) DEFAULT 'Not Specified'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer_info`
--

INSERT INTO `customer_info` (`C_id`, `C_name`, `C_contact`, `C_address`) VALUES
(1, 'Ramlal', 999999999, ''),
(2, 'Shamlal', 999999998, '23/56 bhopal'),
(3, '', 999999997, ''),
(4, 'Mohanlal', 999999996, '344/456 bhopal'),
(5, 'sohamlal', 999999995, '345/546 bhopal'),
(6, 'shubham', 8879000123, 'samta nagar	');

-- --------------------------------------------------------

--
-- Stand-in structure for view `customer_table`
-- (See below for the actual view)
--
CREATE TABLE `customer_table` (
`billing_id` int(20)
,`billing_date` date
,`C_name` varchar(100)
,`C_contact` bigint(15)
,`C_address` varchar(100)
);

-- --------------------------------------------------------

--
-- Table structure for table `items`
--

CREATE TABLE `items` (
  `item_id` int(20) NOT NULL,
  `item_category_id` int(20) NOT NULL,
  `item_brand_id` int(20) NOT NULL,
  `item_name` varchar(100) NOT NULL,
  `item_desc` varchar(500) NOT NULL DEFAULT 'Not specified',
  `item_price` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `items`
--

INSERT INTO `items` (`item_id`, `item_category_id`, `item_brand_id`, `item_name`, `item_desc`, `item_price`) VALUES
(1, 1, 1, 'Asian Paint Red 500ml', 'Extra thin,Light in complexion', 50),
(2, 1, 1, 'Asian Paint Green 1000ml', 'Extra thin,Light in complexion', 30),
(3, 1, 2, 'Ultratech Oil Paint 600ml', 'Extra dark,Glossy', 850),
(4, 2, 3, 'Greenply Moisture resistant 200*200 sqft', 'light weight', 300),
(5, 2, 3, 'Greenply temperature resistant 500*500 sqft', 'flexible', 300),
(6, 2, 3, 'Greenply marine grade 100*100 sqft', 'upto 50m,flexible', 350),
(7, 1, 1, 'Dupli', 'Not specified', 30),
(9, 1, 7, 'hjkjk', '', 76);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `order_id` int(20) NOT NULL,
  `order_item_id` int(20) NOT NULL,
  `order_quantity` int(20) NOT NULL,
  `order_discount` int(20) NOT NULL DEFAULT '0',
  `order_GST%` int(10) NOT NULL DEFAULT '0',
  `order_price` int(10) NOT NULL,
  `order_billing_id` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`order_id`, `order_item_id`, `order_quantity`, `order_discount`, `order_GST%`, `order_price`, `order_billing_id`) VALUES
(1, 2, 3, 100, 18, 2414, 1),
(2, 1, 5, 500, 18, 1324, 2),
(3, 6, 10, 500, 18, 2370, 2),
(4, 4, 1, 50, 18, 150, 3),
(5, 5, 3, 100, 18, 638, 3),
(6, 2, 2, 150, 18, 1526, 3),
(7, 1, 3, 0, 0, 150, 2),
(8, 1, 3, 0, 0, 150, 2),
(9, 1, 2, 0, 0, 100, 2),
(10, 1, 2, 0, 0, 100, 2),
(11, 1, 3, 0, 0, 150, 2),
(12, 1, 3, 0, 0, 150, 2),
(13, 1, 10, 0, 0, 500, 5),
(14, 7, 10, 0, 0, 300, 5);

-- --------------------------------------------------------

--
-- Table structure for table `stock`
--

CREATE TABLE `stock` (
  `stock_id` int(20) NOT NULL,
  `stock_item_id` int(20) NOT NULL,
  `stock_quantity` int(20) NOT NULL,
  `stock_sup_id` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `stock`
--

INSERT INTO `stock` (`stock_id`, `stock_item_id`, `stock_quantity`, `stock_sup_id`) VALUES
(1, 1, 10, 1),
(2, 2, 15, 2),
(3, 3, 10, 1),
(4, 6, 20, 2),
(5, 4, 20, 3),
(6, 5, 20, 2),
(7, 7, 30, 3),
(9, 9, 768, 1);

-- --------------------------------------------------------

--
-- Table structure for table `supplier`
--

CREATE TABLE `supplier` (
  `supp_id` int(20) NOT NULL,
  `supp_name` varchar(50) NOT NULL,
  `supp_address` varchar(100) NOT NULL DEFAULT 'Not specified',
  `supp_contact_1` bigint(15) NOT NULL,
  `supp_contact_2` bigint(15) DEFAULT NULL,
  `supp_email` varchar(50) DEFAULT 'Not specified'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `supplier`
--

INSERT INTO `supplier` (`supp_id`, `supp_name`, `supp_address`, `supp_contact_1`, `supp_contact_2`, `supp_email`) VALUES
(1, 'Sai Nath Trading Co.', '23/65 bhopal', 9000000001, 0, 'sainath@gmail.com'),
(2, 'R K Traders.', '35/62 bhopal', 8000000002, 0, 'rktraders@gmail.com'),
(3, 'Badri Prasad', '33/67 bhopal', 7000000003, 6000000003, 'badriprasad@gmail.com'),
(4, '--Not Selected--', 'Not specified', 0, NULL, 'Not specified');

-- --------------------------------------------------------

--
-- Stand-in structure for view `update_price`
-- (See below for the actual view)
--
CREATE TABLE `update_price` (
`supp_name` varchar(50)
,`item_id` int(20)
,`item_name` varchar(100)
,`item_price` int(10)
,`category_name` varchar(50)
,`brand_name` varchar(50)
,`stock_quantity` int(20)
);

-- --------------------------------------------------------

--
-- Table structure for table `user_info`
--

CREATE TABLE `user_info` (
  `user_id` int(10) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_pass` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_info`
--

INSERT INTO `user_info` (`user_id`, `user_name`, `user_pass`) VALUES
(2, 'customer', 'customer'),
(5, 'pricing', 'pricing'),
(7, 'stocks', 'stock'),
(3, 'supplier', 'supplier'),
(4, 'orders', 'orders'),
(6, 'billing', 'billing'),
(1, 'admin', 'admin');

-- --------------------------------------------------------

--
-- Structure for view `available_stock`
--
DROP TABLE IF EXISTS `available_stock`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `available_stock`  AS  select `s`.`supp_name` AS `supp_name`,`i`.`item_id` AS `item_id`,`i`.`item_name` AS `item_name`,`c`.`category_name` AS `category_name`,`b`.`brand_name` AS `brand_name`,`st`.`stock_quantity` AS `stock_quantity` from ((((`supplier` `s` join `items` `i`) join `category` `c`) join `brand` `b`) join `stock` `st`) where ((`s`.`supp_id` = `st`.`stock_sup_id`) and (`b`.`brand_id` = `i`.`item_brand_id`) and (`c`.`category_id` = `i`.`item_category_id`) and (`i`.`item_id` = `st`.`stock_item_id`)) group by `i`.`item_id` ;

-- --------------------------------------------------------

--
-- Structure for view `customer_table`
--
DROP TABLE IF EXISTS `customer_table`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `customer_table`  AS  select `billing`.`billing_id` AS `billing_id`,cast(`billing`.`billing_datetime` as date) AS `billing_date`,`customer_info`.`C_name` AS `C_name`,`customer_info`.`C_contact` AS `C_contact`,`customer_info`.`C_address` AS `C_address` from (`customer_info` join `billing`) where (`customer_info`.`C_id` = `billing`.`billing_customer_id`) group by `billing`.`billing_id` ;

-- --------------------------------------------------------

--
-- Structure for view `update_price`
--
DROP TABLE IF EXISTS `update_price`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `update_price`  AS  select `supplier`.`supp_name` AS `supp_name`,`items`.`item_id` AS `item_id`,`items`.`item_name` AS `item_name`,`items`.`item_price` AS `item_price`,`category`.`category_name` AS `category_name`,`brand`.`brand_name` AS `brand_name`,`stock`.`stock_quantity` AS `stock_quantity` from ((((`supplier` join `stock`) join `items`) join `category`) join `brand`) where ((`supplier`.`supp_id` = `stock`.`stock_sup_id`) and (`items`.`item_id` = `stock`.`stock_item_id`) and (`category`.`category_id` = `items`.`item_category_id`) and (`brand`.`brand_id` = `items`.`item_brand_id`)) group by `items`.`item_id` ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `billing`
--
ALTER TABLE `billing`
  ADD PRIMARY KEY (`billing_id`),
  ADD KEY `billing_customer_id` (`billing_customer_id`);

--
-- Indexes for table `brand`
--
ALTER TABLE `brand`
  ADD PRIMARY KEY (`brand_id`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `customer_info`
--
ALTER TABLE `customer_info`
  ADD PRIMARY KEY (`C_id`),
  ADD UNIQUE KEY `C_contact` (`C_contact`);

--
-- Indexes for table `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`item_id`),
  ADD KEY `item_category_id` (`item_category_id`,`item_brand_id`),
  ADD KEY `item_brand_id` (`item_brand_id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `order_item_id` (`order_item_id`),
  ADD KEY `order_billing_id` (`order_billing_id`);

--
-- Indexes for table `stock`
--
ALTER TABLE `stock`
  ADD PRIMARY KEY (`stock_id`),
  ADD KEY `stock_item_id` (`stock_item_id`),
  ADD KEY `stock_sup_id` (`stock_sup_id`);

--
-- Indexes for table `supplier`
--
ALTER TABLE `supplier`
  ADD PRIMARY KEY (`supp_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `billing`
--
ALTER TABLE `billing`
  MODIFY `billing_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `brand`
--
ALTER TABLE `brand`
  MODIFY `brand_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `category_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `customer_info`
--
ALTER TABLE `customer_info`
  MODIFY `C_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `items`
--
ALTER TABLE `items`
  MODIFY `item_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `order_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `stock`
--
ALTER TABLE `stock`
  MODIFY `stock_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `supplier`
--
ALTER TABLE `supplier`
  MODIFY `supp_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `billing`
--
ALTER TABLE `billing`
  ADD CONSTRAINT `billing_ibfk_1` FOREIGN KEY (`billing_customer_id`) REFERENCES `customer_info` (`C_id`);

--
-- Constraints for table `items`
--
ALTER TABLE `items`
  ADD CONSTRAINT `items_ibfk_1` FOREIGN KEY (`item_category_id`) REFERENCES `category` (`category_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `items_ibfk_2` FOREIGN KEY (`item_brand_id`) REFERENCES `brand` (`brand_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `items_ibfk_3` FOREIGN KEY (`item_category_id`) REFERENCES `category` (`category_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `items_ibfk_4` FOREIGN KEY (`item_brand_id`) REFERENCES `brand` (`brand_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`order_item_id`) REFERENCES `items` (`item_id`),
  ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`order_billing_id`) REFERENCES `billing` (`billing_id`),
  ADD CONSTRAINT `orders_ibfk_3` FOREIGN KEY (`order_item_id`) REFERENCES `items` (`item_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orders_ibfk_4` FOREIGN KEY (`order_billing_id`) REFERENCES `billing` (`billing_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `stock`
--
ALTER TABLE `stock`
  ADD CONSTRAINT `stock_ibfk_3` FOREIGN KEY (`stock_item_id`) REFERENCES `items` (`item_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `stock_ibfk_4` FOREIGN KEY (`stock_sup_id`) REFERENCES `supplier` (`supp_id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
