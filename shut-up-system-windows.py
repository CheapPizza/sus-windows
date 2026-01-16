if __name__ == "__main__":
    from pycaw.pycaw import AudioUtilities
    import time

    while True:
        sessions = AudioUtilities.GetAllSessions()
        for s in sessions:
            if "AudioSrv.Dll" in s.DisplayName:
                if s.SimpleAudioVolume.GetMasterVolume() > 0.0:
                    s.SimpleAudioVolume.SetMasterVolume(0.0, None)
        time.sleep(60)
