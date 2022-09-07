<%@ Page Language="C#" AutoEventWireup="true" CodeFile="FrmOnlineAdmission.aspx.cs"
    Inherits="Login_FrmOnlineAdmission" %>

<%@ Register Src="~/Login/WucOnlineAdmission.ascx" TagName="WucOnlineAdmission" TagPrefix="uc1" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Student Admission</title>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <link href="../CommonStyleSheet.css" rel="stylesheet" type="text/css" />
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <uc1:WucOnlineAdmission ID="WucOnlineAdmission1" runat="server"></uc1:WucOnlineAdmission>
        </div>
    </form>
</body>
</html>
