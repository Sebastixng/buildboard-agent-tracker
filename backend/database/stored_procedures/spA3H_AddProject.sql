USE BuildBoard;
GO

/******************************************************************************************
** Procedure Name: spA3H_AddProject
** Created By: Your Name
** Created On: 2025-05-09
** Last Modified By: Your Name
** Last Modified On: 2025-05-09
** Primary Application: BLD
** Tags: Project Creation, Project Management
**
** Description:
** Adds a new project to the Projects table with default status "Idea".
**
** Parameters:
** @Title NVARCHAR(255) – The title of the project
** @Niche NVARCHAR(100) – The domain or category of the project
** @Description NVARCHAR(MAX) – A short description of the project
** @Status NVARCHAR(50) – Optional status (default = 'Idea')
**
** Testing Code:
** EXEC spA3H_AddProject @Title = 'AgentPrompt Wizard', @Niche = 'AI Tool', @Description = 'Meta-agent prompt builder'
**
** Notes:
** - Title is required
** - Status defaults to 'Idea'
**
** Copyright © A3H LLC. All rights reserved.
******************************************************************************************/
CREATE PROCEDURE spA3H_AddProject
	@Title NVARCHAR(255)
	,@Niche NVARCHAR(100)
	,@Description NVARCHAR(MAX)
	,@Status NVARCHAR(50) = 'Idea'
AS
BEGIN
	INSERT INTO Projects (Title, Niche, Description, Status)
	VALUES (@Title, @N
