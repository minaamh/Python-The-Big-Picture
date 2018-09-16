import wmi
c = wmi.WMI ()

for s in c.Win32_Service ():
  print (s.ProcessId, s.Name)