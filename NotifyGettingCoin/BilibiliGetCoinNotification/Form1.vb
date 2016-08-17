Imports System.Timers
Imports BilibiliGetCoinNotification.KeyboardHook
Public Class Form1
    'Dim toMinute As Integer = 1000
    Dim toMinute As Integer = 60000
    Private aTimer As System.Timers.Timer
    Private currentInterval As Integer = 3
    Dim hook As KeyboardHook
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Dim response = MsgBox("Start Timer")
        hook = New KeyboardHook()
        AddHandler KeyboardHook.KeyUp, AddressOf keyboardHandler
        If response.Equals(MsgBoxResult.Ok) Then
            aTimer = New System.Timers.Timer()
            aTimer.Interval = currentInterval * toMinute
            AddHandler aTimer.Elapsed, AddressOf UpdateTimer
            aTimer.Enabled = True
        End If
    End Sub
    Private Sub Form1_KeyDown(ByVal sender As Object, ByVal e As KeyEventArgs) Handles MyBase.KeyDown
        If e.KeyCode = Keys.Escape Then
            aTimer.Dispose()
            Close()
        End If
    End Sub
    Private Sub UpdateTimer()
        Select Case currentInterval
            Case 3
                currentInterval = 6
            Case 6
                currentInterval = 10
            Case 10
                currentInterval = 3
        End Select
        aTimer.Stop()
        Dim response = MsgBox("Coins are ready", MsgBoxStyle.OkOnly, "Notification")
        If response.Equals(MsgBoxResult.Ok) Then
            aTimer.Interval = currentInterval * toMinute
            aTimer.Start()
        End If
    End Sub
    Sub keyboardHandler(ByVal Key As Keys)
        If Key.Equals(System.Windows.Forms.Keys.LWin) Then
            Dim response = MsgBox("Do you want to quit the Bilibili Coin Collect Reminder?", MsgBoxStyle.OkCancel, "Notice")
            If response.Equals(MsgBoxResult.Ok) Then
                aTimer.Dispose()
                Close()
            End If
        End If
    End Sub
End Class
