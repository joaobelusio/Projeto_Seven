-- Criação das tabelas principais que não dependem de outras para referência de chave estrangeira
CREATE TABLE `roles` (
  `RoleID` int PRIMARY KEY AUTO_INCREMENT,
  `Name` varchar(255) UNIQUE NOT NULL,
  `UserPermission` TINYINT(1) DEFAULT 1,
  `AffiliatePermission` TINYINT(1) DEFAULT 0,
  `AdminPermission` TINYINT(1) DEFAULT 0
) COMMENT = 'Define os diferentes papéis e suas permissões no sistema de e-commerce.';

CREATE TABLE `categories` (
  `CategoryID` int PRIMARY KEY AUTO_INCREMENT,
  `Name` varchar(255) NOT NULL,
  `Description` text,
  `IsActive` TINYINT(1) DEFAULT 1
) COMMENT = 'Categorias dos itens vendidos na plataforma de e-commerce. Pode incluir produtos, cursos e softwares.';

-- Criação da tabela de produtos após a tabela de categorias, pois existe uma chave estrangeira que depende dela
CREATE TABLE `products` (
  `ProductID` int PRIMARY KEY AUTO_INCREMENT,
  `Name` varchar(255) NOT NULL,
  `Description` text,
  `Price` decimal(10,2) NOT NULL,
  `SKU` varchar(50) UNIQUE NOT NULL,
  `QuantityInStock` int DEFAULT 0,
  `CategoryID` int,
  `ImageURL` varchar(2083),
  `Weight` decimal(10,2),
  `Dimensions` varchar(100),
  `Color` varchar(50),
  `Rating` decimal(3,2),
  `IsActive` TINYINT(1) DEFAULT 1,
  `DateAdded` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `DateModified` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'Detalhes dos produtos listados na plataforma de e-commerce, incluindo estoque e categorização.';

ALTER TABLE `products` ADD FOREIGN KEY (`CategoryID`) REFERENCES `categories` (`CategoryID`);

-- Criação da tabela de usuários, pode ser criada após a tabela de roles por causa da chave estrangeira
CREATE TABLE `users` (
  `UserID` int PRIMARY KEY AUTO_INCREMENT,
  `RoleID` int,
  `FirstName` varchar(255) NOT NULL,
  `LastName` varchar(255) NOT NULL,
  `Email` varchar(255) UNIQUE NOT NULL,
  `PasswordHash` varchar(255),
  `GoogleID` varchar(255) UNIQUE,
  `CPF` varchar(11) UNIQUE NOT NULL,
  `BirthDate` date,
  `IsEmailVerified` TINYINT(1) DEFAULT 0,
  `IsActive` TINYINT(1) DEFAULT 1,
  `DateRegistered` timestamp DEFAULT CURRENT_TIMESTAMP,
  `LastLogin` timestamp,
  `AddressLine1` varchar(255) NOT NULL,
  `AddressLine2` varchar(255),
  `AddressComplement` varchar(255),
  `City` varchar(100) NOT NULL,
  `State` varchar(100) NOT NULL,
  `PostalCode` varchar(20) NOT NULL,
  `Country` varchar(100) NOT NULL
) COMMENT = 'Informações e credenciais das contas de usuários na plataforma de e-commerce.';

ALTER TABLE `users` ADD FOREIGN KEY (`RoleID`) REFERENCES `roles` (`RoleID`);

CREATE TABLE `orders` (
  `OrderID` int PRIMARY KEY AUTO_INCREMENT,
  `UserID` int,
  `Total` decimal(10,2) NOT NULL,
  `OrderStatus` varchar(50) DEFAULT 'pending',
  `PaymentStatus` varchar(50) DEFAULT 'pending',
  `PaymentDetails` text,
  `CreatedAt` timestamp DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` timestamp ON UPDATE CURRENT_TIMESTAMP,
  `AddressLine1` varchar(255) NOT NULL,
  `AddressLine2` varchar(255),
  `City` varchar(100) NOT NULL,
  `State` varchar(100) NOT NULL,
  `PostalCode` varchar(20) NOT NULL,
  `Country` varchar(100) NOT NULL
) COMMENT = 'Detalhes dos pedidos feitos pelos usuários na plataforma de e-commerce.';

ALTER TABLE `orders` ADD FOREIGN KEY (`UserID`) REFERENCES `users` (`UserID`);

CREATE TABLE `order_items` (
  `OrderItemID` int PRIMARY KEY AUTO_INCREMENT,
  `OrderID` int NOT NULL,
  `ProductID` int NOT NULL,
  `Quantity` int NOT NULL,
  `Price` decimal(10,2) NOT NULL,
  `Subtotal` decimal(10,2) NOT NULL
) COMMENT = 'Relaciona os produtos aos pedidos e armazena detalhes específicos dos itens pedidos.';

ALTER TABLE `order_items` ADD FOREIGN KEY (`OrderID`) REFERENCES `orders` (`OrderID`);
ALTER TABLE `order_items` ADD FOREIGN KEY (`ProductID`) REFERENCES `products` (`ProductID`);

CREATE TABLE `coupons` (
  `CouponID` int PRIMARY KEY AUTO_INCREMENT,
  `Code` varchar(255) UNIQUE NOT NULL,
  `Description` text,
  `DiscountType` varchar(50),
  `DiscountPercent` decimal(5,2),
  `DiscountAmount` decimal(10,2),
  `ValidFrom` date,
  `ValidUntil` date,
  `IsActive` TINYINT(1) DEFAULT 1,
  `UsageLimit` int,
  `UsedCount` int DEFAULT 0,
  `MinPurchaseAmount` decimal(10,2)
) COMMENT = 'Gerencia os cupons de desconto e suas regras.';

CREATE TABLE `order_coupons` (
  `OrderCouponID` int PRIMARY KEY AUTO_INCREMENT,
  `OrderID` int NOT NULL,
  `CouponID` int NOT NULL,
  `AppliedDiscountAmount` decimal(10,2)
) COMMENT = 'Registra o uso de cupons em pedidos específicos.';

ALTER TABLE `order_coupons` ADD FOREIGN KEY (`OrderID`) REFERENCES `orders` (`OrderID`);
ALTER TABLE `order_coupons` ADD FOREIGN KEY (`CouponID`) REFERENCES `coupons` (`CouponID`);

CREATE TABLE `affiliate_sales` (
  `AffiliateSaleID` int PRIMARY KEY AUTO_INCREMENT,
  `OrderID` int NOT NULL,
  `UserID` int NOT NULL,
  `Commission` decimal(10,2)
) COMMENT = 'Registra as vendas associadas a cada afiliado e as comissões correspondentes.';

ALTER TABLE `affiliate_sales` ADD FOREIGN KEY (`OrderID`) REFERENCES `orders` (`OrderID`);
ALTER TABLE `affiliate_sales` ADD FOREIGN KEY (`UserID`) REFERENCES `users` (`UserID`);

-- Adicionar mais tabelas e relações conforme necessário