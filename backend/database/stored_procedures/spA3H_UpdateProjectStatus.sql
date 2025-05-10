USE BuildBoard;
GO

/******************************************************************************************
** Procedure Name: spA3H_UpdateProjectStatus
** Created By: Your Name
** Created On: 2025-05-09
** Last Modified By: Your Name
** Last Modified On: 2025-05-09
** Primary Application: BLD
** Tags: Status Change, Project Tracking
**
** Description:
** Updates the status of a project.
**
** Parameters:
** @ProjectID INT – ID of the project
** @NewStatus NVARCHAR(50) – New status value
**
** Testing Code:
** EXEC spA3H_UpdateProjectStatus @ProjectID = 1, @NewStatus = 'In Progress'
**
** Notes:
** - Valid statuses include: Idea, In Progress, Paused, Done
**
** Copyright © A3H LLC. All rights reserved.
******************************************************************************************/
CREATE PROCEDURE spA3H_UpdateProjectStatus
	@ProjectID INT
	,@NewStatus NVARCHAR(50)
AS
BEGIN
	UPDATE Projects
	SET Status = @NewStatus
	WHERE ProjectID = @ProjectID;
END;
GO
