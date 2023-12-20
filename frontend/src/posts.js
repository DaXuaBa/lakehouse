const posts = [
{
    _id: '1',
    name: 'Săn giấc mơ, thách giới hạn',
    image: '/images/1.jpg',
    description:
      'Hãy sẵn sàng bắt đầu cuộc hành trình đầy cảm xúc, khi chúng tôi mang đến một cuộc đua đường mòn theo dấu chân của các người dân tộc thiểu số ngày xưa đi săn kiếm ăn trong rừng núi này. Vào ngày 16 tháng 12, Laan Ultra Trail sẽ đưa bạn vào lòng thiên nhiên, thách thức cả sức mạnh thể chất lẫn bản năng của bạn. Dù bạn săn trải nghiệm, thành tích mới, hãy giải phóng bản năng thợ săn bên trong bạn và chinh phục địa rừng núi, bao quanh bởi vẻ đẹp của thiên nhiên hoang dã nguyên sơ.',
     created_at: "12/12/2023",
    created_user:"Phi công Không Gian"
  },
{
    _id: '2',
    name: 'Vietnam Ulter Run',
    image: '/images/2.jpg',
    description:
      'Giải chạy chinh phục thử thách VIETNAM ULTRA RUN – BEYOND LIMITS là giải chạy đặc biệt và là giải chính thức đầu tiên ở Việt Nam cho cự li dài và siêu dài. Giải chạy nhằm tôn vinh những tinh thần thể thao cao thượng để “Nhanh hơn, Cao hơn, Mạnh hơn, Cùng nhau”.Giải đấu phát huy tinh thần không bỏ cuộc, vượt qua khó khăn, thách thức, và những rào cản để đạt được mục tiêu.',
     created_at: "20/12/2023",
    created_user:"Hổ Báo Trong Nhà"
  },
{
    _id: '3',
    name: 'VnExpress Marathon',
    image: '/images/3.jpg',
    description:
      'Lần đầu tiên được tổ chức trên đất cảng, VnExpress Marathon Hải Phòng có 4 cự ly: 5km, 10km, 21km và 42km. Runner sẽ được sải bước trên các cung đường đi qua những địa điểm nổi tiếng mang tính biểu tượng của thành phố này. Ban tổ chức đang hoàn tất khâu chuẩn bị, dự kiến mở cổng đăng ký vào cuối tháng 12 này.',
     created_at: "22/12/2023",
    created_user:"Rơi Tự Do"
  },
{
    _id: '4',
    name: 'Prenn Trail Challenge',
    image: '/images/4.jpg',
    description:
      'Prenn Trail Challenge là một giải đấu mới với cung đường hoàn toàn khác biệt, đầy trải nghiệm những điểm đặc sắc của Đà Lạt, Lâm Đồng. Với cung đường này, các runners có thể đi qua những rừng thông rào rạt, những con dốc đầy thách thức, trải nghiệm những đồi trà, cà phê vốn là đặc sản của vùng đất cao nguyên tuyệt đẹp này.',
     created_at: "25/12/2023",
    created_user:"Chúa Tể Đám Đông"
  },
{
    _id: '5',
    name: 'HCMC Marathon',
    image: '/images/5.jpg',
    description:
      'HCMC Marathon – Mùa giải thứ 11 sẵn sàng để chào đón bạn! Chạy cùng Thành phố và giành lấy chiến thắng đầu tiên của năm 2024! Giải Marathon Thành phố Hồ Chí Minh hân hạnh mời các bạn tham gia cùng chúng tôi cuộc đua chạy bộ việt dã lớn nhất tại Việt Nam. Giải được tổ chức dưới sự hỗ trợ của Liên đoàn Điền kinh Thành phố Hồ Chí Minh và dưới sự chỉ đạo, hướng dẫn của Sở Văn hóa và Thể thao Tp. Hồ Chí Minh.',
     created_at: "11/11/2023",
    created_user:"Người Lạc Đà Điên"
  },
{
    _id: '6',
    name: 'Run To Live 2024',
    image: '/images/6.jpg',
    description:
      '“Run To Live 2024” ra đời với mục tiêu trở thành một giải chạy thân thuộc với cộng đồng yêu chạy bộ trên khắp lãnh thổ Việt Nam và truyền cảm hứng về tinh thần Run To Live, dự kiến thu hút hơn 6.000 vận động viên trong lần đầu tiên tổ chức.',
     created_at: "12/12/2023",
    created_user:"Nguyễn Nhanh Như Chớp"
  },
{
    _id: '7',
    name: 'Stop And Run Marathon',
    image: '/images/7.jpg',
    description:
      '“Tổ chức vào tháng 5/2024 với các cự ly 5KM, 10KM, 21KM và 42KM. Các Runner sẽ được chạy trên con đường ven biển đẹp nhất Việt Nam, ngắm nhìn bình minh ló dạng, check in với xe nước vàng cam, băng qua cánh đồng điện gió cùng đồi cát trắng tuyệt đẹp. Giải còn mang đến thử thách cho các VĐV ở cự ly 42Km với con dốc cao chưa từng xuất hiện ở bất kỳ giải đấu marathon nào tại Việt Nam.',
     created_at: "5/12/2023",
    created_user:"Dê Đực Quậy Phá"
  },
{
    _id: '8',
    name: 'Tien Phong Marathon',
    image: '/images/8.jpg',
    description:
      '“Giải vô địch quốc gia Marathon và cự ly dài báo Tiền Phong (Tiền Phong Marathon National Championship) là giải đấu đỉnh cao có tuổi đời lâu nhất trong làng thể thao Việt Nam, được tổ chức lần đầu tiên vào năm 1958 tại Hà Nội. Đây là một giải đấu hàng đầu, đã được đưa vào hệ thống thi đấu của điền kinh Việt Nam trong suốt nửa thế kỷ qua, được tổ chức cuối tháng 3 hằng năm. Tiền Phong Marathon quy tụ những VĐV xuất sắc nhất của điền kinh Việt Nam ở các cự ly trung bình và dài tranh tài giành huy chương quốc gia, cũng là cơ hội để các VĐV phong trào tranh tài trên cùng một đường đua với các VĐV hàng đầu quốc gia.',
     created_at: "7/12/2023",
    created_user:"Tiểu Tam Ngốc Nghếch"
  },
{
    _id: '9',
    name: 'International Half Marathon',
    image: '/images/9.jpg',
    description:
      '“Giải bán marathon Quốc tế Việt Nam 2024 (Vietnam International Half Marathon 2024) là giải chạy bộ thuộc hệ thống thi đấu chính thức của Liên đoàn Điền kinh Việt Nam, do Liên đoàn Điền kinh Việt Nam và Uỷ ban nhân dân thành phố Hà Nội tổ chức. ',
     created_at: "11/12/2023",
    created_user:"Quốc Khánh Xanh Mướt"
  },
{
    _id: '10',
    name: 'Discovery Marathon',
    image: '/images/10.jpg',
    description:
      '“Discovery Marathon 2024 sẽ quay lại với những cung đường hòa quyện sắc xanh của thiên nhiên và căng tràn hơi thở dân giã, mộc mạc của những địa danh mà các vận động viên sẽ đặt chân chạy qua.',
     created_at: "19/12/2023",
    created_user:"Đậu Hủ Gia Tộc"
  }
]
export default posts
