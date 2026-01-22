/* =============================================
   TEST 1: DDL & Table Creation
   ============================================= */
USE [MyDatabase];
GO

-- Create table with various constraints
CREATE TABLE [dbo].[Employees] (
    [ID] INT IDENTITY(1,1) PRIMARY KEY,
    [FirstName] NVARCHAR(50) NOT NULL,
    [LastName] NVARCHAR(50) NOT NULL,
    [Salary] FLOAT DEFAULT 0,
    [DepartmentID] INT NULL
);
GO

-- Alter table
ALTER TABLE [dbo].[Employees] ADD [HireDate] INT NULL;
GO

/* =============================================
   TEST 2: Variables & Assignment (The FIX)
   Here we test SELECT without FROM
   ============================================= */
DECLARE @TotalSalary FLOAT;
DECLARE @TaxRate FLOAT;
DECLARE @Message NVARCHAR(100);

SET @TaxRate = 0.15;

-- Previously failing select assignment; should work now
SELECT @TotalSalary = 5000 * (1 + 0.5); 
SELECT @Message = 'Calculation Completed';

-- Accumulate within SELECT
SELECT @TotalSalary += 1000;

PRINT @Message;
GO

/* =============================================
   TEST 3: Control Flow & DML
   ============================================= */
IF @TotalSalary > 2000
BEGIN
    INSERT INTO [dbo].[Employees] (FirstName, LastName, Salary)
    VALUES ('Ali', 'Ahmed', 6500);

    UPDATE [dbo].[Employees]
    SET Salary = Salary * 1.1
    WHERE ID = 1;
END
ELSE
BEGIN
    DELETE FROM [dbo].[Employees] WHERE Salary < 1000;
END
GO

/* =============================================
   TEST 4: Complex SELECT with JOIN & CASE
   ============================================= */
SELECT TOP 10 
    E.FirstName, 
    E.LastName,
    CASE 
        WHEN E.Salary > 5000 THEN 'High'
        ELSE 'Normal'
    END AS SalaryGrade
FROM [dbo].[Employees] AS E
LEFT JOIN [dbo].[Departments] AS D ON E.DepartmentID = D.ID
WHERE E.Salary IS NOT NULL AND E.FirstName LIKE 'A%'
ORDER BY E.Salary DESC;
GO

/* =============================================
   TEST 5: Try Catch & Dynamic Execution
   ============================================= */
BEGIN TRY
    DECLARE @SQL NVARCHAR(MAX);
    SET @SQL = 'SELECT * FROM NonExistentTable';
    
    -- Execute dynamic statement
    EXEC sp_executesql @SQL;
END TRY
BEGIN CATCH
    DECLARE @ErrorMsg NVARCHAR(4000);
    DECLARE @ErrorSev INT;

    -- Select variables inside CATCH
    SELECT 
        @ErrorMsg = ERROR_MESSAGE(),
        @ErrorSev = ERROR_SEVERITY();
        
    PRINT 'Error Occurred: ' + @ErrorMsg;
END CATCH
GO
