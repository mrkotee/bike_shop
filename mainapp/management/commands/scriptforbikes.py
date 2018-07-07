from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Bike, BikeImages
from django.core.files import File
import os


# b1 = Bike(name='BERGAMONT Revox 4.0 2015', brand='BERGAMONT', model_art='15-MTB-H-9076', bike_type='MNTN', 
# 	description='Lead the pace with this fast cross country racer. The Revox accelerates like you would not believe and has all its angles precisely dialed to make for the ultimate 29er mountainbike geometry. When you first get on the bike you will feel immediately at home and very soon after that the imminent urge to push forward. A wide range of models is available from full-on race bikes with a revamped carbon fibre frame to entry-level models built on an aluminium frame that has not only has the same geometry and shape as its high-end counterpart, but also features the tricked-out internal cable routing.', 
# 	cost=300 , wheeldia=29, color='Green', weight=14.2)
# b1_img = BikeImages(os.path.join(os.getcwd, 'static/images/bik1.jpg'), b1)


class Command(BaseCommand):
    def handle(self, *args, **options):
        bikes_names = ['BERGAMONT Revox 4.0 2015', 'SPECIALIZED CR2-2014',
                       'Specialized Rockhopper Comp 29', 'Specialized 2017 Crosstrail Disc',
                       'Specialized Jett 29', 'SPECIALIZED MYKA HT']
        bikes_brand = ['BERGAMONT', 'SPECIALIZED', 'SPECIALIZED', 'SPECIALIZED', 'SPECIALIZED', 'SPECIALIZED']
        # bikes_arts = [r'15-MTB-H-9076', r'EV193851-9000-1', r'RhComp 29/16', ]
        bikes_types = ['MNTN', 'RB', 'MNTN', 'MNTN', 'MNTN', 'MNTN']
        bikes_costs = [300, 450, 600, 600, 499, 350]
        bikes_wheels = [29, 28, 29, 28, 29, 26]
        bikes_speeds = [27, 16, 20, 24, 20, 21]
        bikes_colors = ['Green', 'White', 'White', 'Blue', 'White', 'Black']
        bikes_weights = [14.2, 8.8, 12.0, 14.1, 11.3, 12.4]
        bikes_descriptions = [
            'Lead the pace with this fast cross country racer. The Revox accelerates like you would not believe and has all its angles precisely dialed to make for the ultimate 29er mountainbike geometry. When you first get on the bike you will feel immediately at home and very soon after that the imminent urge to push forward. A wide range of models is available from full-on race bikes with a revamped carbon fibre frame to entry-level models built on an aluminium frame that has not only has the same geometry and shape as its high-end counterpart, but also features the tricked-out internal cable routing.',
            'The Specialized Allez Elite Road Bike has been designed to provide the discerning cyclist with a comfortable, efficient ride for everything from long-distance escapades to short distance spins to the nearest cafe. Constructed from a durable E5 premium aluminium, the frame is strong and durable, whilst the capable range of components keep you riding with more confidence.',
            "Whether you've been riding trails for decades or you're just starting to cut your teeth, the Rockhopper Comp 29 will take your rides to the next level. We built it with just the right balance between performance and durability, and not to toot our own horn, but we nailed it. The Comp 29 features corrosion-resistant hardware for long wear, our Trail 29 Geometry that provides confident handling and efficiency, and an alloy frame construction that's equal parts light and compliant.",
            "When you're at the gym, you use equipment that works for you. Likewise, you need a bike that performs exactly how you need it to—versatile, comfortable, and efficient. That's why our Crosstrail Disc comes equipped with a custom suspension fork with a lockout feature for fast and efficient use over any surface. To build on this blend of comfort and speed, the frame is built from lightweight A1 Premium aluminum tubing with a geometry that's made to fit just right from the minute you get on the bike. Add in a selection of strong, no-fuss components, reliable mechnical disc brakes, and rack/fender mounts, and you get a bike that's ready to roll wherever you choose to take it.",
            "With its premium aluminum frame and durable component package, the Jett 29 is a rugged, hard-working trailblazer that'll help you get out there and crush all the Cross Country terrain you can find. Built with performance, reliability, and efficiency in mind, the Jett is snappy, quick, and graceful over rugged terrain, and will help you reach—and smash—your goals, whether they be getting your best race result ever, or besting your own PRs on local trails.",
            "For fun and effortless trail adventure, the redesigned Myka HT is the best looking and best riding recreational hardtail that still comes at a killer value. Featuring lightweight aluminum frame designs with ultra low standover height, 80 to 100mm travel forks and capable components, the Myka gives even the newest rider the control and confidence to leave the pavement behind."
        ]

        # bikes = []
        # bikes_imgs = []
        # model_art = bikes_arts[i]
        for i in range(6):
            b = Bike(name=bikes_names[i], brand=bikes_brand[i], bike_type=bikes_types[i],
                     description=bikes_descriptions[i],
                     cost=bikes_costs[i], wheeldia=bikes_wheels[i], color=bikes_colors[i], weight=bikes_weights[i])
            # bikes.append(b)
            b.save()
            img_path = 'bik{}.jpg'.format(str(i + 1))
            # pathi =
            img_file = open(os.path.join(os.getcwd(), 'static/images/', img_path), 'rb')
            djan_file = File(img_file)
            b_img = BikeImages()
            b_img.bike = b
            b_img.image.save(img_path, djan_file, save=True)
            img_file.close()
        # bikes_imgs.append(b_img)
