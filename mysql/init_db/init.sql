USE tiki;
go
CREATE TABLE tiki.product (
  id_product bigint Not NULL primary key,
  sku text,
  product_name text,
  url_key text,
  url_path text,
  availability int,
  seller_id bigint,
  seller_name text,
  price bigint DEFAULT NULL,
  original_price bigint DEFAULT NULL,
  discount bigint DEFAULT NULL,
  discount_rate bigint DEFAULT NULL,
  review_count bigint DEFAULT NULL,
  rating_average bigint DEFAULT NULL,
  primary_category_path text,
  primary_category_name text DEFAULT NULL,
  productset_id bigint DEFAULT NULL,
  seller_product_id bigint DEFAULT NULL,
  thumbnail_url text DEFAULT NULL,
  video_url text
);