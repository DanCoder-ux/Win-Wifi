import subprocess

R = "\033[91m"
W = "\033[0m"

def banner():
    print('''\n
                                                                           Et
                         L.                                                E#t
                     t   EW:        ,ft                             t      E##t     t
            ;        Ej  E##;       t#E                    ;        Ej     E#W#t    Ej
          .DL        E#, E###t      t#E                  .DL        E#,    E#tfL.   E#,
  f.     :K#L     LWLE#t E#fE#f     t#E          f.     :K#L     LWLE#t    E#t      E#t
  EW:   ;W##L   .E#f E#t E#t D#G    t#E ........ EW:   ;W##L   .E#f E#t ,ffW#Dffj.  E#t
  E#t  t#KE#L  ,W#;  E#t E#t  f#E.  t#E  eeeeee  E#t  t#KE#L  ,W#;  E#t  ;LW#ELLLf. E#t
  E#t f#D.L#L t#K:   E#t E#t   t#K: t#E          E#t f#D.L#L t#K:   E#t    E#t      E#t
  E#jG#f  L#LL#G     E#t E#t    ;#W,t#E          E#jG#f  L#LL#G     E#t    E#t      E#t
  E###;   L###j      E#t E#t     :K#D#E          E###;   L###j      E#t    E#t      E#t
  E#K:    L#W;       E#t E#t      .E##E          E#K:    L#W;       E#t    E#t      E#t
  EG      LE.        E#t ..         G#E          EG      LE.        E#t    E#t      E#t
  ;       ;@         ,;.             fE          ;       ;@         ,;.    ;#t      ,;.
                                      ,                                     :;       ;
    \n\n''')

if __name__ == "__main__":
    banner()
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
    datas = meta_data.decode('utf-8', errors="backslashreplace").split('\n')

    profiles = []

    for data in datas:
        if "All User Profile" in data:
            data = data.split(':')[1][1:-1]

            profiles.append(data)

    print("\n\t\t\t{:<30} | {:<}".format(" SSID", "Password"))
    print("\t\t\t----------------------------------------------")

    try:
        for ssid in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', ssid, 'key=clear'])
            results = results.decode('utf-8', errors="backslashreplace").split('\n')

            results = [ b.split(':')[1][1:-1] for b in results if "Key Content" in b ]

            try:
                print("\t\t\t {:<30}| {:<}".format(ssid, results[0]))

            except IndexError:
                print("\t\t\t {:<30}| {:<}".format(ssid, ""))

    except subprocess.CalledProcessError:
        print(f'\n\t\t\t\t{R}[{W}-{R}]{W} Encoding Error Occurred... :(')

    print("\n")
