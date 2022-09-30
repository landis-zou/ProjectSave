using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using Newtonsoft.Json;

public class UserLocalData
{
    private static UserLocalData mInstance;
    private string path = Application.persistentDataPath + "/" + GlobeSetting.USER_INFO;
    
    public static UserLocalData getInstance()
    {
        if (mInstance == null)
        {
            mInstance = new UserLocalData();
        }
        return mInstance;
    }
    
    public void test()
    {
        Debug.Log(Application.persistentDataPath);

        TestJsonData data = new TestJsonData();

        data.userid = "900625";
        data.userdata.Add("username", "KK");
        data.userdata.Add("useName", "Ekey");
        data.nickname = "Landis";


        var a = JsonConvert.SerializeObject(data);

        var b = JsonConvert.DeserializeObject<TestJsonData>(a);


        TestData data2;
        data2.TestString = "Landis";

        if(File.Exists(path))
        {

        }


    }
}
