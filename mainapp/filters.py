from django.db.models import Q


class ProductFilter:

    FILTERSET = {
        "product_name": lambda x: Q(name__icontains=x),
        "min_price": lambda x: Q(total_price__gte=x),
        "max_price": lambda x: Q(total_price__lte=x)
    }


    def filter_products(self, products, data):
        result_filter = Q()
        for elem in data:
            # products = products.filter(
            #     self.FILTERSET[elem](
            #         data[elem]
            #     )
            # )
            result_filter.add(
                self.FILTERSET[elem](
                    data[elem]
                ), Q.AND
            )

        return products.filter(result_filter)