USE BuildBoard;
GO

/******************************************************************************************
** Procedure Name: spA3H_AddLogEntry
** Created By: Your Name
** Created On: 2025-05-09
** Last Modified By: Your Name
** Last Modified On: 2025-05-09
** Primary Application: BLD
** Tags: Project Logs, Updates
**
** Description:
** Adds a progress log entry for a specific project.
**
** Parameters:
** @ProjectID INT – ID of the project
** @Entry NVARCHAR(MAX) – Log text content
**
** Testing Code:
** EXEC spA3H_AddLogEntry @ProjectID = 1, @Entry = 'Finished UI layout for prompt wizard'
**
** Notes:
** - Must be linked to an existing ProjectID
**
** Copyright © A3H LLC. All rights reserved.
******************************************************************************************/
CREATE PROCEDURE spA3H_AddLogEntry
	@ProjectID INT
	,@Entry NVARCHAR(MAX)
AS
BEGIN
	INSERT INTO Logs (ProjectID, Entry)
	VALUES (@ProjectID, @Entry);
END;
GO
