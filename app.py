import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import matplotlib.pyplot as mp


st.title("GREEN FARM",)


label = "I. Project Introduction"
s = f"<p style='font-size:20px; color:#000000;font-weight: bold;' >{label}</p>"
st.markdown(s, unsafe_allow_html=True)


st.write("Project Idea: Land rental service for growing vegetables in Ho Chi Minh City")
st.write("Location: Nha Be , Ho Chi Minh city")
label = "Main Service"
s = f"<p style='font-size:15px; color:#000000;font-weight: bold;' >{label}</p>"
st.markdown(s, unsafe_allow_html=True)

st.write("- Provision of agricultural land")
st.write("- Vegetable care service")
st.write("- Harvest, packaging and deliver")
st.write("- Create agricultural place for outdoor activities")
label = "Vision"
s = f"<p style='font-size:15px; color:#000000;font-weight: bold;' >{label}</p>"
st.markdown(s, unsafe_allow_html=True)

st.write("Becoming a leading enterprise in the field of agricultural land rental services in Ho Chi Minh city")
label = "Mission"
s = f"<p style='font-size:15px; color:#000000;font-weight: bold;' >{label}</p>"
st.markdown(s, unsafe_allow_html=True)

st.write("Build green space for residents to improve standard of living in Ho Chi Minh city with “GREEN FARM, Experience Life”")
label = "II. Secondary Data"
s = f"<p style='font-size:20px; color:#000000;font-weight: bold;' >{label}</p>"
st.markdown(s, unsafe_allow_html=True)
# Hinh 18
import matplotlib.pyplot as plt
import numpy as np

plt.clf()

x1 = list(range(2018, 2030, 1))
y1 = [76.7, 79.8, 82.96, 86.28, 89.73, 93.32, 102.65, 112.91, 124.21, 136.63, 150.29, 158.56]

xs = np.array(x1)
ys = np.array(y1)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(xs, ys, 'bo-', color='black')  # Thêm tham số color='black'

ax.text(2018, 76.7, '76.7', fontsize=10, ha='right')
ax.text(2022, 89.73, '89.73', fontsize=10, ha='right')
ax.text(2023, 93.3, '93.3', fontsize=10, ha='right')
ax.text(2029, 158.56, '158.56', fontsize=10, ha='right')
st.write("The Global Agro Rural Tourism Market 2018 - 2029")
st.pyplot(fig)
st.write("The global agro-rural tourism market is divided into three insight segments: direct-market agritourism, experience and education agritourism, and event and recreation agritourism. These segments are able to satisfy all consumers needs and expectations through agritourism.")
st.write("The Global Agro-Rural Tourism Market is expected to reach close to USD 158.56 billion by 2029 with an annualized growth rate of 8% - 30%.")
label = "III. Data Survey"
s = f"<p style='font-size:20px; color:#000000;font-weight: bold;' >{label}</p>"
st.markdown(s, unsafe_allow_html=True)

st.write("We surveyed people in Ho Chi Minh City with sample n = 442")

data = pd.read_excel('/content/drive/MyDrive/Khảo sát.xlsx')
st.dataframe(data)

label = "1. The Age"
s = f"<p style='font-size:15px; color:#000000;font-weight: bold;' >{label}</p>"
st.markdown(s, unsafe_allow_html=True)
# hinh 1
texxt= ["2.5%", "17.6", "20.4", "25.1","23.3","11.1"]
labels = ['Dưới 18 tuổi  ','Từ 18 tuổi đến dưới 28 tuổi','Từ 28 tuổi đến dưới 35 tuổi','Từ 35 tuổi đến dưới 45 tuổi','Từ 45 tuổi đến dưới 55 tuổi','Từ 55 tuổi trở lên ']
values = [2.5, 17.6, 20.4, 25.1,23.3,11.1]
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.update_traces(marker=dict(colors=['#00CD00', '#00FF7F','#00EE00','#006400','#008B00','#00FF00','#00CD00']))
fig.update_layout(title_text = "Anh/Chị bao nhiêu tuổi?")
st.plotly_chart(fig)


#hinh 2
labels = ['Học sinh/Sinh viên','Nhân viên văn phòng','Công Nhân','Đã nghỉ ','Khác']
values = [14.5, 51.1, 12, 10.9, 11.5]
fig1 = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig1.update_traces(marker=dict(colors=['#008B00','#006400','#00CD00','#00EE00','#00FF00']))
fig1.update_layout(title_text = "Nghề nghiệp hiện tại của Anh/Chị?")

label = "2. Occupation"
s = f"<p style='font-size:15px; color:#000000;font-weight: bold;' >{label}</p>"
st.markdown(s, unsafe_allow_html=True)
st.plotly_chart(fig1)

#hinh 3
labels = ['Dưới 5 triệu','Từ 5 triệu - Dưới 10 triệu','Từ 10 triệu - Dưới 15 triệu','Từ 15 triệu - Dưới 20 triệu','Từ 20 triệu - Dưới 30 triệu','Trên 30 triệu']
values = [11.8,15.8, 5.7, 16.3, 23.8, 26.7]

fig2 = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig2.update_traces(marker=dict(colors=['#00FF00','#00EE00','#00CD00','#00FF7F','#008B00','#006400']))
fig2.update_layout(title_text = "Mức thu nhập bình quân đầu người trong hộ gia đình của Anh/Chị?")

label = "3. The income level"
s = f"<p style='font-size:15px; color:#000000;font-weight: bold;' >{label}</p>"
st.markdown(s, unsafe_allow_html=True)
st.plotly_chart(fig2)


label = "4. Marital status"
s = f"<p style='font-size:15px; color:#000000;font-weight: bold;' >{label}</p>"
st.markdown(s, unsafe_allow_html=True)
st.write("Marital status: Married: 73.5% and Single: 26.5%")


#hinh 4
labels = ['Thành phố Thủ Đức','Quận 1, Quận 3, Quận 5, Quận 8, Quận 10, Quận 11','Bình Thạnh, Phú Nhuận, Gò Vấp, Tân Bình','Quận 6, Bình Tân, Bình Chánh, Tân Phú','Quận 4, Quận 7, Nhà Bè, Cần Giờ','Quận 12, Hóc Môn, Củ Chi']
values = [33.9,27.8, 17.9, 6.8, 9.7, 3.8]

fig3 = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig3.update_traces(marker=dict(colors=['#006400','#008B00','#00CD00', '#00EE00','#00FF00','#00FF7F']))
fig3.update_layout(title_text = "Anh/Chị đang sinh sống ở khu vực nào tại TP.HCM?")

label = "5. Location"
s = f"<p style='font-size:15px; color:#000000;font-weight: bold;' >{label}</p>"
st.markdown(s, unsafe_allow_html=True)
st.plotly_chart(fig3)
st.write("We have surveyed all of districts in Ho Chi Minh City. ")

#Hinh 4
import plotly.graph_objects as go
texts = ["58.4%", "33%", "95.7%"]
fig4 = go.Figure(go.Bar(
            x=[58.4, 33, 95.7],
            y=['Khu vui chơi, giải trí, sở thú', 'Học năng khiếu (Học vẽ, hát, múa,…)', 'Các hoạt động ngoài trời khác'],
            orientation='h'))
fig4.update_traces(texttemplate = texts,
                  textposition = "inside",
                  marker_color = 'green')
fig4.update_layout(title_text = 'Anh/Chị thường dẫn gia đình đi đâu vào cuối tuần?')

label = "6. Outdoor activities participation"
s = f"<p style='font-size:15px; color:#000000;font-weight: bold;' >{label}</p>"
st.markdown(s, unsafe_allow_html=True)
st.plotly_chart(fig4)

#Hinh 5
labels = ['Thường xuyên (2 tuần 1 lần)','Rất thường xuyên (1 tuần 1 lần)','Thỉnh thoảng (vài tháng 1 lần)','Không','Hiếm khi (1 năm 1 lần)','Luôn luôn (mỗi ngày)']
values = [50.2,31, 7.7, 6.8, 4.1, 0.2]

fig5 = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig5.update_traces(marker=dict(colors=['#006400','#008B00','#00CD00', '#00EE00','#00FF00','#00FF7F']))
fig5.update_layout(title_text = "Anh/Chị có thường xuyên tham gia các hoạt động ngoài trời (cụ thể là đi du lịch sinh thái, tham quan nông trại, …) cùng gia đình không? ")
st.plotly_chart(fig5)

#Hinh 6
tet= ["93.2%", "64.7%", "44.1%"]
fig6 = go.Figure(data=[go.Bar(
    x=['Nội thành TP.HCM', 'Vùng ven TP.HCM', 'Tỉnh'],
    y=[93.2, 64.7, 44.1])])

fig6.update_layout(title_text='Anh/chị thường tham gia các hoạt động ngoài trời như trên ở đâu?',

                  xaxis_tickfont_size=15,
                  yaxis=dict(

        titlefont_size=30,
        tickfont_size=15,
        ))
fig6.update_layout(height=700, width = 800)

fig6.update_traces(width=0.5, marker_color='green',
                  texttemplate = tet)
st.plotly_chart(fig6)

#Hình 7
texs=["62.4%", "93.7%", "44.1%", "23.1%"]
fig7 = go.Figure(data=[go.Bar(
    x=['Gắn kết gia đình', 'Giảm stress, thư giãn ', 'Hỗ trợ con cái phát triển tốt',
       'Niềm vui, sở thích tuổi già '],
    y=[62.4, 93.7, 44.1, 23.1])]
      )

fig7.update_layout(title_text='Tại sao anh/chị quyết định tham gia các hoạt động ngoài trời?',
                  xaxis_tickfont_size=10,
                  yaxis=dict(

        titlefont_size=20,
        tickfont_size=10,
        ))
fig7.update_layout(height=700, width = 800)
fig7.update_traces(marker_color='green',width=0.6,
                  texttemplate = texs)
st.plotly_chart(fig7)
st.write("When customers have a stable source of income, they will think about needs such as outdoor activities on weekends or holidays to relax with their family. Especially families with children, according to UNI-HABITAT (Perera L., Nam J., 2023), children's rights and needs for child - friendly nature-based playground model, knowledge and experience sharing.")
#Hinh 8
texs=["74.9%", "90.3%", "0.9%"]
fig8 = go.Figure(data=[go.Bar(
    x=['Chợ truyền thống ', 'Siêu thị, Cửa hàng tiện lợi ', 'Khác'],
    y=[74.9, 90.3, 0.9])]
      )

fig8.update_layout(title_text='Anh/chị thường mua rau từ đâu?',
                  xaxis_tickfont_size=10,
                  yaxis=dict(

        titlefont_size=20,
        tickfont_size=10,
        ))
fig8.update_layout(height=700, width = 800)
fig8.update_traces(marker_color='green',width=0.6,
                  texttemplate = texs)

label = "7. Consumption Habits"
s = f"<p style='font-size:15px; color:#000000;font-weight: bold;' >{label}</p>"
st.markdown(s, unsafe_allow_html=True)
st.plotly_chart(fig8)

#Hinh 9
texs=["10%", "17.4%", "11.8%", "23.5%","37.3%"]
fig9 = go.Figure(data=[go.Bar(
    x=['Không quan tâm', 'Ít quan tâm ', 'Có quan tâm',
       'Quan tâm','Rất quan tâm'],
    y=[10, 17.4, 11.8, 23.5,37.3])]
      )

fig9.update_layout(title_text='Anh/chị có quan tâm đến vấn đề dư lượng hóa chất độc hại trong rau hay không?',
                  xaxis_tickfont_size=10,
                  yaxis=dict(

        titlefont_size=20,
        tickfont_size=10,
        ))
fig9.update_layout(height=700, width = 800)
fig9.update_traces(marker_color='green',width=0.6,
                  texttemplate = texs)
st.plotly_chart(fig9)
st.write("According to a survey of 442 people living in Ho Chi Minh City, the results showed that up to 60.8% were very concerned about the issue of chemicals and pesticides in vegetables. This is a large number, showing that consumers are increasingly concerned about food safety issues.")


#Hinh 10
labels = ['Từ 750.000đ – Dưới 900.000đ','Từ 900.000đ trở lên','Dưới 600.000đ','Từ 600.000đ – Dưới 750.000đ']
values = [39.6,31,26, 3.4]

fig10 = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig10.update_traces(marker=dict(colors=['#006400','#008B00','#00CD00', '#00EE00','#00FF00','#00FF7F']))
fig10.update_layout(title_text = "Anh/chị chi tiêu khoảng bao nhiêu tiền để mua rau trong 1 tháng?")
st.plotly_chart(fig10)

#Hinh 11
labels = ['20%','25%','30%','35%','40%']
values = [41.2, 32.8, 24, 1.8, 0]

fig11 = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig11.update_traces(marker=dict(colors=['#006400','#008B00','#00CD00', '#00EE00','#00FF00','#00FF7F']))
fig11.update_layout(title_text = "Anh/chị sẵn sàng trả thêm bao nhiêu tiền cho các sản phẩm rau củ an toàn, không chứa dư lượng chất hóa học độc hại?")
st.plotly_chart(fig11)

st.write("Anh/chị có thích trồng, thu hoạch, và dùng rau tự tay mình trồng không?")
st.write("Có: 72.9%, Không: 27.1%")
#Hinh12
ts = ["9%", "36%", "59.7%"]
fig12 = go.Figure(go.Bar(
            x=[9, 36, 59.7],
            y=['Nhà có đất trồng', 'Trồng rau bằng chậu', 'Không trồng'],
            orientation='h'))
fig12.update_traces(marker=dict(color='#006400'),
                  width=0.5,
                  text=ts)
fig12.update_layout(title_text="Anh/chị thường trồng rau như thế nào?")

label = "8. Growing Vegetables Habit"
s = f"<p style='font-size:15px; color:#000000;font-weight: bold;' >{label}</p>"
st.markdown(s, unsafe_allow_html=True)
st.plotly_chart(fig12)

#Hinh 13
te=["28.73%", "28.28%", "27.83%", "25.57%", "35.29%", "56.11%"]
fig13 = go.Figure(data=[go.Bar(
    x=["Rau muống","Rau mồng tơi","Rau dền","Cải ngọt, cải xanh","Rau thơm","Khác"],
    y=[28.73, 28.28, 27.83, 25.57, 35.29, 56.11])])

fig13.update_layout(title_text='Anh/chị thường trồng những loại rau gì?',

                  xaxis_tickfont_size=15,
                  yaxis=dict(

        titlefont_size=30,
        tickfont_size=15,
        ))
fig13.update_layout(height=900, width = 1000)

fig13.update_traces(width=0.5, marker_color='green',texttemplate = te)
st.plotly_chart(fig13)

#Hinh 14
ts = ["52.5%", "90%", "68.3%"]
fig14 = go.Figure(go.Bar(
            x=[52.5, 90, 68.3],
            y=['Không có thời gian', 'Không có không gian (Khu vườn để trồng rau)', 'Không biết cách chăm sóc '],
            orientation='h'))
fig14.update_traces(marker=dict(color='#006400'),
                  width=0.5,
                  text=ts)
fig14.update_layout(title_text="Cản trở lớn nhất trì hoãn sở thích trồng rau của anh/chị tại TP.HCM là gì?")
st.plotly_chart(fig14)
st.write("The concerns of customers such as caring about food quality and safety and wanting to experience agricultural activities, customers also encounter many difficulties when growing vegetables at home: 52.5% do not have time, 90% there is not enough space for planting, 68.3% do not know how to take care of them.")
st.write("According to above question(Anh/Chị thường trồng rau như thế nào?), 59.7% do not grow its because of not enough spaces to vegetables. This means customers likes growing vegetables and any plants, but they do not have spaces.")

label = "Children participate outdoor activities"
s = f"<p style='font-size:15px; color:#000000;font-weight: bold;' >{label}</p>"
st.markdown(s, unsafe_allow_html=True)
st.write("Anh/chị có nghĩ rằng việc cho con cái trải nghiệm trồng rau sẽ giúp chúng rèn luyện sự kiên nhẫn, giúp trẻ nâng cao được sức đề kháng và phát triển toàn diện?")
st.write("Có: 62.4%, Không: 37.6%")
st.write("Parents encourage children to participate in outdoor activities to rapid brain development and children are curious to explore new things, so playing can help them discover many things about themselves (Dan Tri News, 2023). Especially, encouraged agricultural practices like plowing and planting vegetables will make children like to eat vegetables more through the Green Farm survey with sample 442.")


label = "9. The demand for agricultural land rental service"
s = f"<p style='font-size:15px; color:#000000;font-weight: bold;' >{label}</p>"
st.markdown(s, unsafe_allow_html=True)
st.write("Anh/chị có sẵn sàng sử dụng dịch vụ cho thuê đất trồng rau với 1 ô đất khoảng 10m vuông tại Nhà Bè, Thành phố Hồ Chí Minh không?")
st.write("Có: 53.2%, Không: 46.8%")
st.write("The result of this question is 53.2% that looking for empty spaces or plots of land to grow vegetables and any plants they want")
#Hinh 15
labels = ['Từ 750.000đ – Dưới 900.000đ/tháng','Từ 600.000đ – Dưới 750.000đ/tháng','Không sử dụng','Từ 900.000đ trở lên','Dưới 600.000đ']
values = [30.8, 14.3, 44.3, 6.1, 4.5]

fig15 = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig15.update_traces(marker=dict(colors=['#006400','#008B00','#00CD00', '#00EE00','#00FF00','#00FF7F']))
fig15.update_layout(title_text = "Anh/Chị mong muốn thuê 10m2 đất để trồng rau với giá bao nhiêu?")
st.plotly_chart(fig15)
st.write("The price of each plot (10m2) which customers want is from 750.000 VND to 900.000 VND.")

#Hinh 16
labels = ['Qua Camera','Gửi ảnh qua Zalo','Cả 2 ý ']
values = [5.7, 7.9, 86.4]

fig16 = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig16.update_traces(marker=dict(colors=['#006400','#008B00','#00CD00', '#00EE00','#00FF00','#00FF7F']))
fig16.update_layout(title_text = "Anh/chị muốn theo dõi vườn rau đã thuê 24/24 thông qua thiết bị nào?")
st.plotly_chart(fig16)

#Hinh 17
labels = ['Không quan tâm','Ít quan tâm','Có quan tâm','Quan tâm','Rất quan tâm']
values = [14, 23.1, 12.7,19.7,30.5]

fig20 = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig20.update_traces(marker=dict(colors=['#00CD00', '#00EE00','#00FF00','#00FF7F','#008B00','#006400']))
fig20.update_layout(title_text = "Mức độ quan tâm của anh/chị và gia đình nếu Green Farm tổ chức các buổi workshop vào cuối tuần hướng dẫn các phương pháp trồng, chăm sóc rau")

label = "More activities and services for customers's experience such as free workshop, fruit gardens sight-seeing"
s = f"<p style='font-size:15px; color:#000000;font-weight: bold;' >{label}</p>"
st.markdown(s, unsafe_allow_html=True)
st.plotly_chart(fig20)
label = "Level of concern's customers in other services"
s = f"<p style='font-size:15px; color:#000000;font-weight: bold;' >{label}</p>"
st.markdown(s, unsafe_allow_html=True)
st.write("Ngoài dịch vụ cho thuê đất trồng rau, anh/chị có sẵn sàng sử dụng thêm các dịch vụ khác như DV chăm sóc rau, tham quan vườn rau & vườn trái cây tại Green Farm không?")
st.write("Có: 52.7%, Không: 47.3%")

label = "10. Customer Persona"
s = f"<p style='font-size:15px; color:#000000;font-weight: bold;' >{label}</p>"
st.markdown(s, unsafe_allow_html=True)




data = pd.read_excel("/content/drive/MyDrive/Colab Notebooks/1.xlsx")
st.write(data)
st.write("This is customer persona's Green Farm. Target customers is in Ho Chi Minh City, who like to experience farming activities and grow vegetables.")

label = "IV. Financial Green Farm"
s = f"<p style='font-size:20px; color:#000000;font-weight: bold;' >{label}</p>"
st.markdown(s, unsafe_allow_html=True)

import plotly.graph_objects as go

Labels = ['Year 1', 'Year 2', 'Year 3', 'Year 4',
      'Year 5', 'Year 6','Year 7','Year 8']

REVENUE = [2327892494,3022070992,3681865191,4602198229,5090359145,5532646560,5538338160,5545168080]
PROFIT = [-462150771,13528825,422688823,860851394,1137311005,1337584082,1278684456,1218083602]


percent_có = ['2.3B','3B','3.6B','4.6B','5.09B','5.5B','5.5B','5.5B']
percent_không = ['-462.1M','13.5M','422.7M','422M','860.8M','1.1B','1.3B','1.27B','1.21B']

fig22 = go.Figure(
    data=[
        go.Bar(name='REVENUE', x=Labels, y=REVENUE, text=percent_có, textposition='auto', marker_color='#33CC33',width=0.38),
        go.Bar(name='PROFIT', x=Labels, y=PROFIT, text=percent_không, textposition='auto', marker_color='#006400',width = 0.38)
    ]
)

# Cập nhật layout của biểu đồ
fig22.update_layout(
    title_text='Doanh Thu của Green Farm trong vòng 8 năm (VND)',
    barmode='group'  # Đặt chế độ hiển thị của cột là nhóm
)
st.write("Revenue and Profit in 8 years (VND)")
st.plotly_chart(fig22)




















