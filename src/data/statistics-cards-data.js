import {
  BanknotesIcon,
  UserPlusIcon,
  UsersIcon,
  ChartBarIcon,
  ArrowLongUpIcon,
  InboxIcon,
  CircleStackIcon 
  
} from "@heroicons/react/24/solid";

export const statisticsCardsData = [
  {
    color: "gray",
    icon: BanknotesIcon,
    title: "Overall Gain",
    value: "$53,000",
    footer: {
      color: "text-green-500",
      value: "+55%",
      label: "than last year",
    },
  },
  {
    color: "gray",
    icon: ArrowLongUpIcon,
    title: "Today's Gain",
    value: "1,034",
    footer: {
      color: "text-green-500",
      value: "+3%",
      label: "than yesterday",
    },
  },
  {
    color: "gray",
    icon: CircleStackIcon ,
    title: "Total Amount",
    value: "156,430",
    footer: {
      color: "text-red-500",
      value: "20%",
      label: "last one year",
    },
  },
  {
    color: "gray",
    icon: ChartBarIcon,
    title: "Total Investment",
    value: "$103,430",
    footer: {
      color: "text-green-500",
      value: "+10%",
      label: "last one year",
    },
  },
];

export default statisticsCardsData;
