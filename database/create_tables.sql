/* *************************************************************
   Drop and Create the tables for the shopping_mall database.
   Entities:   store, promotion
   Cross-ref:  store_promotion_xref (many-to-many)
   *************************************************************** */

-- Switch to shopping_mall database
USE `shopping_mall`

-- Drop tables in child-to-parent order so foreign keys don't block the drop
DROP TABLE IF EXISTS `store_promotion_xref`;
DROP TABLE IF EXISTS `store`;
DROP TABLE IF EXISTS `promotion`;

-- ---------------------------------------------------------------
-- Create the store table
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `store` (
    `id` int(11) NOT NULL,
    `store_name` varchar(100) NOT NULL,
    `category` varchar(50) NOT NULL,
    `unit_number` varchar(10) NOT NULL,
    `floor_level` int(11) NOT NULL,
    `phone` varchar(20) NOT NULL,
    `lease_start_date` date NOT NULL,
    `is_active` tinyint(1) NOT NULL DEFAULT 1
);

-- Designate the `id` column as the primary key
ALTER TABLE `store`
    ADD PRIMARY KEY (`id`);

-- Make `id` column auto increment on inserts
ALTER TABLE `store`
    MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

-- ---------------------------------------------------------------
-- Create the promotion table
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `promotion` (
    `id` int(11) NOT NULL,
    `promotion_name` varchar(100) NOT NULL,
    `description` varchar(255) NOT NULL,
    `discount_percent` decimal(5,2) NOT NULL,
    `start_date` date NOT NULL,
    `end_date` date NOT NULL,
    `is_active` tinyint(1) NOT NULL DEFAULT 1
);

-- Designate the `id` column as the primary key
ALTER TABLE `promotion`
    ADD PRIMARY KEY (`id`);

-- Make `id` column auto increment on inserts
ALTER TABLE `promotion`
    MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

-- ---------------------------------------------------------------
-- Create the store_promotion_xref cross-reference table
-- Resolves the many-to-many relationship between store and promotion:
--   a promotion applies to many stores, a store participates in
--   many promotions.
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `store_promotion_xref` (
    `store_id` int(11) NOT NULL,
    `promotion_id` int(11) NOT NULL
);

-- Composite primary key: a store can only be linked to a given
-- promotion once
ALTER TABLE `store_promotion_xref`
    ADD PRIMARY KEY (`store_id`, `promotion_id`);

-- Foreign key back to the store table
ALTER TABLE `store_promotion_xref`
    ADD CONSTRAINT `fk_xref_store`
    FOREIGN KEY (`store_id`) REFERENCES `store` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

-- Foreign key back to the promotion table
ALTER TABLE `store_promotion_xref`
    ADD CONSTRAINT `fk_xref_promotion`
    FOREIGN KEY (`promotion_id`) REFERENCES `promotion` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE;
