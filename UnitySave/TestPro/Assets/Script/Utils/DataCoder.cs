using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class DataCoder
{
    private static DataCoder m_Instance;

    private static List<char> m_binEncodeKey = new List<char> { (char)1, (char)32, (char) 200 };

    public static DataCoder getInstance()
    {
        if(m_Instance == null)
        {
            m_Instance = new DataCoder();
            m_Instance.init();
        }

        return m_Instance;
    }

    public void init ()
    {
    }

    /// <summary>
    /// 存储string型值
    /// </summary>
    public void saveValue(string key, string value)
    {

    }

    /// <summary>
    /// 存储int型值
    /// </summary>
    public void saveValue(string key, int value)
    {

    }

    /// <summary>
    /// 存储long型值
    /// </summary>
    public void saveValue(string key, long value)
    {

    }

    /// <summary>
    /// 存储double型值
    /// </summary>
    public void saveValue(string key, double value)
    {

    }

    /// <summary>
    /// 存储float型值
    /// </summary>
    public void saveValue(string key, float value)
    {

    }

    /// <summary>
    /// 存储bool型值
    /// </summary>
    public void saveValue(string key, bool value)
    {

    }

    /// <summary>
    /// 存储string-List类型值
    /// </summary>
    public void saveList(string key, List<string> valueList)
    {

    }

    /// <summary>
    /// 存储int-List类型值
    /// </summary>
    public void saveList(string key, List<int> valueList)
    {
        
    }

    /// <summary>
    /// 存储long-List类型值
    /// </summary>
    public void saveList(string key, List<long> valueList)
    {

    }

    /// <summary>
    /// double-List类型值
    /// </summary>
    public void saveList(string key, List<double> valueList)
    {

    }

    /// <summary>
    /// float-List类型值
    /// </summary>
    public void saveList(string key, List<float> valueList)
    {

    }

    /// <summary>
    /// bool-List类型值
    /// </summary>
    public void saveList(string key, List<bool> valueList)
    {

    }

    /// <summary>
    /// 存储string, string-Dictionary类型值
    /// </summary>
    public void saveDictionary(string key, Dictionary<string, string> valueDic)
    {

    }

    /// <summary>
    /// 存储string, int-Dictionary类型
    /// </summary>
    public void saveDictionary(string key, Dictionary<string, int> valueDic)
    {

    }

    /// <summary>
    /// 存储string, long-Dictionary类型
    /// </summary>
    public void saveDictionary(string key, Dictionary<string, long> valueDic)
    {

    }

    /// <summary>
    /// 存储string, double-Dictionary类型
    /// </summary>
    public void saveDictionary(string key, Dictionary<string, double> valueDic)
    {

    }

    /// <summary>
    /// 存储string, float-Dictionary类型
    /// </summary>
    public void saveDictionary(string key, Dictionary<string, float> valueDic)
    {

    }

    /// <summary>
    /// 存储string, bool-Dictionary类型
    /// </summary>
    public void saveDictionary(string key, Dictionary<string, bool> valueDic)
    {

    }
}
