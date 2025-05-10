USE BuildBoard;
GO

/******************************************************************************************
** Procedure Name: spA3H_GetProjectOverview
** Created By: Your Name
** Created On: 2025-05-09
** Last Modified By: Your Name
** Last Modified On: 2025-05-09
** Primary Application: BLD
** Tags: Project Overview, Log Preview
**
** Description:
** Returns project info along with the most recent log entry.
**
** Parameters:
** @ProjectID INT – ID of the project to retrieve
**
** Testing Code:
** EXEC spA3H_GetProjectOverview @ProjectID = 1
**
** Notes:
** - Includes project meta and latest log only
**
** Copyright © A3H LLC. All rights reserved.
******************************************************************************************/
CREATE PROCEDURE spA3H_GetProjectOverview
	@ProjectID INT
AS
BEGIN
	SELECT
		P.ProjectID
		,P.Title
		,P.Niche
		,P.Description
		,P.Status
		,P.CreatedAt
		,LastLog.Entry AS LatestLog
		,LastLog.CreatedAt AS LogDate
	FROM Projects P
	OUTER APPLY (
		SELECT TOP 1 Entry, CreatedAt
		FROM Logs
		WHERE ProjectID = P.ProjectID
		ORDER BY CreatedAt DESC
	) AS LastLog
	WHERE P.ProjectID = @ProjectID;
END;
GO
