# Banco de Dados do Projeto SEVEN E-commerce

## Visão Geral

Este diretório contém os artefatos de modelagem do banco de dados para o sistema de e-commerce SEVEN. A estrutura do banco de dados é projetada para apoiar todas as operações essenciais de uma plataforma de e-commerce, incluindo gerenciamento de produtos, usuários, pedidos, afiliados e cupons de desconto.

## Estrutura do Banco de Dados

O banco de dados é modelado para refletir as seguintes entidades principais:

- `products`: Contém todos os dados referentes aos produtos disponíveis na plataforma.
- `users`: Armazena informações dos usuários registrados, incluindo dados pessoais e credenciais de login.
- `roles`: Define os diferentes papéis de usuários dentro do sistema e suas permissões associadas.
- `affiliate_sales`: Rastreia as vendas e comissões geradas por afiliados.
- `coupons`: Gerencia os cupons de desconto que podem ser aplicados aos pedidos.
- `order_coupons`: Associa cupons utilizados a pedidos específicos.
- `orders`: Mantém registros dos pedidos realizados na plataforma, incluindo status e detalhes de pagamento.
- `order_items`: Detalha cada produto que compõe um pedido.
- `categories`: Categoriza os itens vendidos na plataforma, como produtos, cursos e softwares.

Cada tabela está estruturada com colunas que representam os atributos pertinentes para cada entidade. As tabelas estão inter-relacionadas para permitir uma complexa gestão e recuperação de dados.

## Modelagem

O banco de dados foi modelado utilizando o MySQL e segue as melhores práticas de normalização para garantir a integridade e eficiência dos dados. Abaixo está um resumo das tabelas e suas principais colunas:

### Tabelas e Colunas Principais

- `products`: `ProductID`, `Name`, `Price`, `SKU`, `QuantityInStock`, `CategoryID`, etc.
- `users`: `UserID`, `FirstName`, `LastName`, `Email`, `CPF`, `AddressLine1`, etc.
- `roles`: `RoleID`, `Name`, `UserPermission`, `AffiliatePermission`, `AdminPermission`.
- `affiliate_sales`: `AffiliateSaleID`, `OrderID`, `UserID`, `Commission`.
- `coupons`: `CouponID`, `Code`, `DiscountType`, `DiscountPercent`, `DiscountAmount`.
- `order_coupons`: `OrderCouponID`, `OrderID`, `CouponID`, `AppliedDiscountAmount`.
- `orders`: `OrderID`, `UserID`, `Total`, `OrderStatus`, `PaymentStatus`.
- `order_items`: `OrderItemID`, `OrderID`, `ProductID`, `Quantity`, `Price`.
- `categories`: `CategoryID`, `Name`, `Description`.

## Implementação

Os scripts SQL para criação das tabelas e quaisquer migrações necessárias podem ser encontrados neste diretório. A implementação e manutenção do banco de dados devem ser realizadas por um DBA ou desenvolvedor com conhecimento adequado de MySQL e práticas de segurança de banco de dados.

Para mais detalhes sobre cada tabela e como importar o modelo para uma ferramenta de modelagem, consulte os comentários detalhados dentro de cada arquivo `.sql` ou `.dbml`.

## Contribuindo

Para contribuir com o modelo de banco de dados, por favor, siga as diretrizes de contribuição no arquivo CONTRIBUTING.md principal deste repositório.

---

Todos os direitos reservados. SEVEN E-commerce © [Ano Atual].
