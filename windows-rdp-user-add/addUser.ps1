 $user = New-LocalUser -AccountNeverExpires:$true -Password ( ConvertTo-SecureString -AsPlainText -Force 'testtest') -Name "Paul" -FullName "Paul" -Description "Local Administrator"
 Add-LocalGroupMember -Group "Administrators" -Member $user
 Add-LocalGroupMember -Group "Remote Desktop Users" -Member $user