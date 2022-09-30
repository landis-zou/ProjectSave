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
/// class��������,��C/C++����Ľṹ����һ�µ��÷�
/// ����C#����,Struct�����������ʾ
/// ������ȷ���������,�Լ�ͨ��class��Struct������ѡ�ջ֮�������
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
/// struct��C#����,�����¶���Ϊֵ����,�������ݲ�������Ż�
/// ����ʹ�ø�����������,��ʹ����Ҫ�����¶��������,�Ƽ�Class,����
/// </summary>
struct TestData
{
    public int TestInt;
    public string TestString;
    public float TestFloat;
}

