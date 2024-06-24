CREATE TABLE IF NOT EXISTS "users"(
    "Id" TEXT PRIMARY KEY, 
    "Name" TEXT NOT NULL, 
    "Gender" TEXT, 
    "Age" INTEGER,
    "Birthdate" DATE, 
    "Address" TEXT
);
CREATE TABLE IF NOT EXISTS "stores"(
    "Id" TEXT PRIMARY KEY, 
    "Name" TEXT NOT NULL, 
    "Type" TEXT, 
    "Address" TEXT
);
CREATE TABLE IF NOT EXISTS "orders"(
    "Id" TEXT PRIMARY KEY, 
    "OrderAt" DATETIME NOT NULL, 
    "StoreId" TEXT NOT NULL, 
    "UserId" TEXT NOT NULL,
    FOREIGN KEY ("StoreId") REFERENCES "stores"("Id"),  -- "stores"("Id") => "stores.Id"
    FOREIGN KEY ("UserId") REFERENCES "useres"("Id")    -- => "users.Id" 이렇게도 작성 가능
);
CREATE TABLE IF NOT EXISTS "items"(
    "Id" TEXT PRIMARY KEY, 
    "Name" TEXT NOT NULL, 
    "Type" TEXT, 
    "UnitPrice" INTEGER -- 미국 달러면 REAL을 통해 소수점 지원
);
CREATE TABLE IF NOT EXISTS "orderitems"(
    "Id" TEXT PRIMARY KEY, 
    "OrderId" TEXT NOT NULL, 
    "ItemId" TEXT,
    FOREIGN KEY ("orderId") REFERENCES "orders"("Id"),  -- => "orders.Id"
    FOREIGN KEY ("ItemId") REFERENCES "items"("Id")     -- => "items.Id"
);