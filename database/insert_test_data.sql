/* ******************************************************
   Insert test data into the shopping_mall database.
   ******************************************************** */

-- Switch to the shopping_mall database.
USE `shopping_mall`

-- ---------------------------------------------------------------
-- Insert data into the store table.
-- ---------------------------------------------------------------
INSERT INTO `store` (store_name, category, unit_number, floor_level, phone, lease_start_date, is_active)
VALUES ('Bright Threads', 'Apparel', '101', 1, '703-555-0111', '2022-03-01', 1);

INSERT INTO `store` (store_name, category, unit_number, floor_level, phone, lease_start_date, is_active)
VALUES ('Tech Nook', 'Electronics', '102', 1, '703-555-0112', '2021-11-15', 1);

INSERT INTO `store` (store_name, category, unit_number, floor_level, phone, lease_start_date, is_active)
VALUES ('Sole Station', 'Footwear', '210', 2, '703-555-0113', '2023-01-10', 1);

INSERT INTO `store` (store_name, category, unit_number, floor_level, phone, lease_start_date, is_active)
VALUES ('The Reading Room', 'Books & Media', '215', 2, '703-555-0114', '2020-06-20', 1);

INSERT INTO `store` (store_name, category, unit_number, floor_level, phone, lease_start_date, is_active)
VALUES ('Garden Fresh Cafe', 'Food & Beverage', '305', 3, '703-555-0115', '2024-02-05', 1);

INSERT INTO `store` (store_name, category, unit_number, floor_level, phone, lease_start_date, is_active)
VALUES ('Glow Cosmetics', 'Beauty', '108', 1, '703-555-0116', '2023-08-12', 1);

INSERT INTO `store` (store_name, category, unit_number, floor_level, phone, lease_start_date, is_active)
VALUES ('Home & Hearth', 'Home Goods', '220', 2, '703-555-0117', '2019-09-30', 0);

INSERT INTO `store` (store_name, category, unit_number, floor_level, phone, lease_start_date, is_active)
VALUES ('Playtime Toys', 'Toys & Games', '112', 1, '703-555-0118', '2022-12-01', 1);

-- ---------------------------------------------------------------
-- Insert data into the promotion table.
-- ---------------------------------------------------------------
INSERT INTO `promotion` (promotion_name, description, discount_percent, start_date, end_date, is_active)
VALUES ('Back to School Savings', 'Discounts on apparel, electronics, and books', 15.00, '2026-08-01', '2026-08-31', 1);

INSERT INTO `promotion` (promotion_name, description, discount_percent, start_date, end_date, is_active)
VALUES ('Summer Kickoff Sale', 'Storewide summer discount event', 20.00, '2026-06-01', '2026-06-30', 0);

INSERT INTO `promotion` (promotion_name, description, discount_percent, start_date, end_date, is_active)
VALUES ('Holiday Shopping Extravaganza', 'Major holiday season discount event', 25.00, '2026-11-20', '2026-12-31', 0);

INSERT INTO `promotion` (promotion_name, description, discount_percent, start_date, end_date, is_active)
VALUES ('Weekend Flash Sale', 'Two-day flash discount for select stores', 10.00, '2026-07-18', '2026-07-19', 1);

INSERT INTO `promotion` (promotion_name, description, discount_percent, start_date, end_date, is_active)
VALUES ('New Season Refresh', 'Discount on new seasonal arrivals', 12.50, '2026-09-01', '2026-09-15', 0);

-- ---------------------------------------------------------------
-- Insert data into the store_promotion_xref table.
-- Links each promotion to the stores participating in it.
-- ---------------------------------------------------------------

-- Back to School Savings (promotion_id 1): apparel, electronics, books
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (1, 1);
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (2, 1);
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (4, 1);

-- Summer Kickoff Sale (promotion_id 2): storewide, all active stores
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (1, 2);
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (2, 2);
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (3, 2);
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (4, 2);
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (5, 2);
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (6, 2);
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (8, 2);

-- Holiday Shopping Extravaganza (promotion_id 3): storewide, all active stores
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (1, 3);
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (2, 3);
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (3, 3);
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (4, 3);
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (5, 3);
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (6, 3);
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (8, 3);

-- Weekend Flash Sale (promotion_id 4): select stores only
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (3, 4);
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (6, 4);
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (8, 4);

-- New Season Refresh (promotion_id 5): apparel and footwear
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (1, 5);
INSERT INTO `store_promotion_xref` (store_id, promotion_id) VALUES (3, 5);
