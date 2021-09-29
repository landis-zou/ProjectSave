using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

public class UserLocalData
{
    private static UserLocalData mInstance;

    public static UserLocalData getInstance()
    {
        if (mInstance == null)
        {
            mInstance = new UserLocalData();
        }
        return mInstance;
    }
    
    //private
    public void test()
    {
        Debug.Log(Application.persistentDataPath);


        StreamWriter sw;
        FileInfo fi = new FileInfo(Application.persistentDataPath + "/" + GlobeSetting.USER_INFO);

        if (!fi.Exists)
        {
            sw = fi.CreateText();
        }
        else
        {
            sw = fi.AppendText();
        }

        sw.WriteLine("Hello World");
        sw.Close();
    }

    public void test2()
    {
        StreamWriter sw;
        FileInfo fi = new FileInfo(Application.persistentDataPath + "//" + GlobeSetting.USER_INFO);

        if (!fi.Exists)
        {
            sw = fi.CreateText();
        }
        else
        {
            sw = fi.AppendText();
        }
        
    }

}
