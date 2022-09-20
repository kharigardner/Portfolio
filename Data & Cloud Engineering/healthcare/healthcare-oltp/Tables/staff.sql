/* this script creates the staff table for the healthcare transactional database */

CREATE TABLE [dbo].[staff]
(
  [Id] INT NOT NULL PRIMARY KEY
  , [FirstName] VARCHAR(50) NOT NULL
  , [LastName] VARCHAR(50) NOT NULL
  , [DepartmentID] INT NOT NULL
  , [Title] VARCHAR(50) NOT NULL
  , [IsActive] BIT NOT NULL
  , [CreatedDate] DATETIME NOT NULL
  , [CreatedBy] VARCHAR(50) NOT NULL
  , [ModifiedDate] DATETIME NOT NULL
  , [ModifiedBy] VARCHAR(50) NOT NULL
  , [DeletedDate] DATETIME NULL
  , [DeletedBy] VARCHAR(50) NULL
)

/* we may not need the created and modified dates and by fields, as Microsoft introduced ledger capabilities in SQL Server 2016, but we will keep them for now */
