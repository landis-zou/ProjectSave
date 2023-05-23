using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.U2D;
using UnityEngine.UI;
using Newtonsoft.Json;
using System.IO;

public class TestScript : MonoBehaviour
{
    public Button mButton;
    

    // Start is called before the first frame update
    void Start()
    {
        UserLocalData.getInstance().test();

        SpriteAtlas atlas = AssetDatabase.LoadAssetAtPath<SpriteAtlas>("Assets/achievement/achievement.spriteatlas");

        var a = atlas.GetSprite("pro_hero_pur");
        
        mButton.image.sprite = a;

        int b = 0;

        test(b);
    }

    // Update is called once per frame
    void Update()
    {

    }

    void test(int value)
    {
        var mPath = Application.persistentDataPath + "/" + GlobeSetting.USER_INFO;

        Debug.Log(Application.persistentDataPath);

        TestJsonData data = new TestJsonData();

        data.userid = "900625";
        data.userdata.Add("username", "KK");
        data.userdata.Add("useName", "Ekey");
        data.nickname = "Landis";
        data.testMap.Add(TestEnum.TestCount, 789);
        data.testMap.Add(TestEnum.TestCount2, "so");
        //data.testMap.Add("7799", "Cool");


        var a = JsonConvert.SerializeObject(data);

        var b = JsonConvert.DeserializeObject<TestJsonData>(a);


        var c = b.testMap[TestEnum.TestCount];


        TestData data2;
        data2.TestString = "Landis";

        if (File.Exists(mPath))
        {
            File.WriteAllText(mPath, a);
        }


    }

}

/// <summary>
/// class��������,��C/C++����Ľṹ����һ�µ��÷�
/// ����C#����,Struct�����������ʾ
/// ������ȷ���������,�Լ�ͨ��class��Struct������ѡ�ջ֮�������
/// </summary>
class TestJsonData
{
    public string userid;
    public string nickname;
    public Hashtable userdata;
    public Dictionary<TestEnum, object> testMap;


    public TestJsonData()
    {
        userid = "";
        nickname = "";
        userdata = new Hashtable();
        testMap = new Dictionary<TestEnum, object>();
    }
    
};

/// <summary>
/// struct��C#����,�����¶���Ϊֵ����,�������ݲ�������Ż�
/// ����ʹ�ø�����������,��ʹ����Ҫ�����¶��������,�Ƽ�Class,����
/// </summary>
struct TestData
{
    public int TestInt;
    public string TestString;
    public float TestFloat;
}

enum TestEnum
{
    TestCount,
    TestCount2,
}



