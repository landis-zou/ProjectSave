using System;
using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.U2D;
using UnityEngine.UI;

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
        value = 2;
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
    public Dictionary<jvalue, jvalue> testMap;

    public TestJsonData()
    {
        userid = "";
        nickname = "";
        userdata = new Hashtable();
        testMap = new Dictionary<jvalue, jvalue>();
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

