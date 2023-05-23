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
/// class定义数据,与C/C++里面的结构体是一致的用法
/// 但在C#里面,Struct增加了诸多显示
/// 更加明确对象的作用,以及通过class与Struct来区别堆、栈之间的区别
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
/// struct在C#里面,被重新定义为值类型,进行数据层的性能优化
/// 不可使用复杂数据类型,如使用需要生成新对象的数据,推荐Class,如上
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



